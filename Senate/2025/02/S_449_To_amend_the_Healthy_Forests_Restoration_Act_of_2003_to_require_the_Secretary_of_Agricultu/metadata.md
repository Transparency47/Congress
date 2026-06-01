# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/449?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/449
- Title: Expediting Forest Restoration and Recovery Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 449
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-02-02T17:35:58Z
- Update date including text: 2026-02-02T17:35:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S794)
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S794)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/449",
    "number": "449",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Expediting Forest Restoration and Recovery Act of 2025",
    "type": "S",
    "updateDate": "2026-02-02T17:35:58Z",
    "updateDateIncludingText": "2026-02-02T17:35:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S794)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-02-06T17:48:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "SD"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s449is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 449\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Thune (for himself and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Healthy Forests Restoration Act of 2003 to require the Secretary of Agriculture to expedite hazardous fuel or insect and disease risk reduction projects on certain National Forest System land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Expediting Forest Restoration and Recovery Act of 2025 .\n#### 2. Application by Forest Service of authorities to expedite environmental analyses in carrying out hazardous fuel and insect and disease risk reduction projects\nSection 104 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6514 ) is amended by adding at the end the following:\n(i) Application by Forest Service of authorities To expedite environmental analyses in carrying out hazardous fuel and insect and disease risk reduction projects (1) Definitions In this subsection: (A) Insect and disease treatment area The term insect and disease treatment area means an area that\u2014 (i) is designated by the Secretary as an insect and disease treatment area under this title; or (ii) is designated as at-risk or a hazard on the most recent National Insect and Disease Risk Map published by the Forest Service. (B) Secretary The term Secretary has the meaning given the term in section 101(14)(A). (2) Use of authorities In carrying out a hazardous fuel or insect and disease risk reduction project authorized under this Act in an insect and disease treatment area, the Secretary shall\u2014 (A) apply the categorical exclusion established by section 603 if the project is carried out in an insect and disease treatment area\u2014 (i) designated as suitable for timber production within the applicable forest plan; or (ii) where timber harvest activities are not prohibited; (B) conduct applicable environmental assessments and environmental impact statements in accordance with this section if the project is carried out in\u2014 (i) an insect and disease treatment area\u2014 (I) outside of an area described in subparagraph (A); or (II) where other significant resource concerns exist, as determined exclusively by the Secretary; or (ii) an insect and disease treatment area equivalent to not less than a Hydrologic Unit code 5 watershed, as defined by the United States Geological Survey; and (C) notwithstanding subsection (d), in the case of any other hazardous fuel or insect and disease risk reduction project, in the environmental assessment or environmental impact statement prepared under subsection (b), study, develop, and describe\u2014 (i) the proposed agency action; and (ii) the alternative of no action. (3) Priority for reducing risks of insect infestation and wildfire Except where established as a mandatory standard that constrains project and activity decisionmaking in a resource management plan (as defined in section 101(13)(A)) in effect on the date of enactment of this Act, in the case of an insect and disease treatment area, the Secretary shall prioritize reducing the risks of insect and disease infestation and wildfire over other planning objectives. (4) Inclusion of Fire Regime Group IV Notwithstanding section 603(c)(2)(B), the Secretary shall apply the categorical exclusion described in paragraph (2)(A) to areas in Fire Regime Group IV. (5) Excluded areas This subsection shall not apply to\u2014 (A) a component of the National Wilderness Preservation System; or (B) an inventoried roadless area, except in the case of an activity that is permitted under\u2014 (i) the final rule of the Secretary entitled Special Areas; Roadless Area Conservation (66 Fed. Reg. 3244 (January 12, 2001)); or (ii) a State-specific roadless area conservation rule. (6) Reports The Secretary shall annually make publicly available data describing the acreage treated under hazardous fuel or insect and disease risk reduction projects in insect and disease treatment areas during the previous year. .\n#### 3. Good neighbor authority\nSection 8206(b)(2) of the Agricultural Act of 2014 ( 16 U.S.C. 2113a(b)(2) ) is amended by striking subparagraph (C) and inserting the following:\n(C) Treatment of revenue Funds received from the sale of timber by a Governor of a State under a good neighbor agreement shall be retained and used by the Governor\u2014 (i) to carry out authorized restoration services under that good neighbor agreement; and (ii) if funds remain after carrying out authorized restoration services under clause (i), to carry out authorized restoration services within the State under other good neighbor agreements. .",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-03-12T17:08:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s449",
          "measure-number": "449",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-02-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s449v00",
            "update-date": "2026-02-02"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Expediting Forest Restoration and Recovery Act of 2025</strong></p><p>This bill excludes from environmental review certain projects that reduce the risk of damage to National Forests from wildfires\u00a0or insect infestations. It also makes permanent the authority for states to retain and use revenues from good neighbor agreement timber sales\u00a0for certain restoration services.</p><p>The bill exempts such projects from federal environmental review requirements if the projects are carried out in (1) insect and disease treatment areas where timber harvest activities are allowed; or (2) areas in Fire Regime Group IV, which are areas that typically burn every 35-200 years with high severity. However, the exemption does not apply to National Wilderness Preservation System lands or certain roadless areas.</p><p>The Forest Service must conduct an environmental review for such a project if it is carried out in (1) an area where significant resource concerns exist; or (2) an insect and disease treatment area larger than a certain size.</p><p>In the case of environmental reviews of other projects addressing wildfires or insect infestations, the Forest Service\u00a0only must describe (1) the proposed agency action, and (2) the alternative of no agency action.\u00a0</p><p>In insect and disease treatment areas,\u00a0the Forest Service must\u00a0prioritize reducing the risks of insect infestations and wildfires over other objectives in forest plans.</p>"
        },
        "title": "Expediting Forest Restoration and Recovery Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s449.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expediting Forest Restoration and Recovery Act of 2025</strong></p><p>This bill excludes from environmental review certain projects that reduce the risk of damage to National Forests from wildfires\u00a0or insect infestations. It also makes permanent the authority for states to retain and use revenues from good neighbor agreement timber sales\u00a0for certain restoration services.</p><p>The bill exempts such projects from federal environmental review requirements if the projects are carried out in (1) insect and disease treatment areas where timber harvest activities are allowed; or (2) areas in Fire Regime Group IV, which are areas that typically burn every 35-200 years with high severity. However, the exemption does not apply to National Wilderness Preservation System lands or certain roadless areas.</p><p>The Forest Service must conduct an environmental review for such a project if it is carried out in (1) an area where significant resource concerns exist; or (2) an insect and disease treatment area larger than a certain size.</p><p>In the case of environmental reviews of other projects addressing wildfires or insect infestations, the Forest Service\u00a0only must describe (1) the proposed agency action, and (2) the alternative of no agency action.\u00a0</p><p>In insect and disease treatment areas,\u00a0the Forest Service must\u00a0prioritize reducing the risks of insect infestations and wildfires over other objectives in forest plans.</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119s449"
    },
    "title": "Expediting Forest Restoration and Recovery Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Expediting Forest Restoration and Recovery Act of 2025</strong></p><p>This bill excludes from environmental review certain projects that reduce the risk of damage to National Forests from wildfires\u00a0or insect infestations. It also makes permanent the authority for states to retain and use revenues from good neighbor agreement timber sales\u00a0for certain restoration services.</p><p>The bill exempts such projects from federal environmental review requirements if the projects are carried out in (1) insect and disease treatment areas where timber harvest activities are allowed; or (2) areas in Fire Regime Group IV, which are areas that typically burn every 35-200 years with high severity. However, the exemption does not apply to National Wilderness Preservation System lands or certain roadless areas.</p><p>The Forest Service must conduct an environmental review for such a project if it is carried out in (1) an area where significant resource concerns exist; or (2) an insect and disease treatment area larger than a certain size.</p><p>In the case of environmental reviews of other projects addressing wildfires or insect infestations, the Forest Service\u00a0only must describe (1) the proposed agency action, and (2) the alternative of no agency action.\u00a0</p><p>In insect and disease treatment areas,\u00a0the Forest Service must\u00a0prioritize reducing the risks of insect infestations and wildfires over other objectives in forest plans.</p>",
      "updateDate": "2026-02-02",
      "versionCode": "id119s449"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s449is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Expediting Forest Restoration and Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:38:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Expediting Forest Restoration and Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Healthy Forests Restoration Act of 2003 to require the Secretary of Agriculture to expedite hazardous fuel or insect and disease risk reduction projects on certain National Forest System land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:45Z"
    }
  ]
}
```
