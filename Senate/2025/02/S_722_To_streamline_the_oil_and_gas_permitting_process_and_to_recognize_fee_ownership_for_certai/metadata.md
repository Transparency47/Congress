# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/722
- Title: Bureau of Land Management Mineral Spacing Act
- Congress: 119
- Bill type: S
- Bill number: 722
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-05-04T18:11:14Z
- Update date including text: 2026-05-04T18:11:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/722",
    "number": "722",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Bureau of Land Management Mineral Spacing Act",
    "type": "S",
    "updateDate": "2026-05-04T18:11:14Z",
    "updateDateIncludingText": "2026-05-04T18:11:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
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
          "date": "2025-02-25T19:43:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "WY"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "ND"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s722is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 722\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mr. Hoeven (for himself, Mr. Barrasso , Mr. Cramer , and Mr. Daines ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo streamline the oil and gas permitting process and to recognize fee ownership for certain oil and gas drilling or spacing units, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bureau of Land Management Mineral Spacing Act .\n#### 2. Compliance with BLM permitting\n##### (a) In general\nNotwithstanding the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ), the Federal Oil and Gas Royalty Management Act of 1982 ( 30 U.S.C. 1701 et seq. ), or subpart 3162 of part 3160 of title 43, Code of Federal Regulations (or successor regulations), but subject to any applicable State or Tribal requirements and subsection (c), the Secretary of the Interior shall not require a permit to drill for an oil and gas lease under the Mineral Leasing Act ( 30 U.S.C. 181 et seq. ) for an action occurring within an oil and gas drilling or spacing unit if\u2014\n**(1)**\nthe Federal Government\u2014\n**(A)**\nowns less than 50 percent of the minerals within the oil and gas drilling or spacing unit; and\n**(B)**\ndoes not own or lease the surface estate within the area directly impacted by the action;\n**(2)**\nthe well is located on non-Federal land overlying a non-Federal mineral estate, but some portion of the wellbore enters and produces from the Federal mineral estate subject to the lease; or\n**(3)**\nthe well is located on non-Federal land overlying a non-Federal mineral estate, but some portion of the wellbore traverses but does not produce from the Federal mineral estate subject to the lease.\n##### (b) Notification\nFor each State permit to drill or drilling plan that would impact or extract oil and gas owned by the Federal Government\u2014\n**(1)**\neach lessee of Federal minerals in the unit, or designee of a lessee, shall\u2014\n**(A)**\nnotify the Secretary of the Interior of the submission of a State application for a permit to drill or drilling plan on submission of the application; and\n**(B)**\nprovide a copy of the application described in subparagraph (A) to the Secretary of the Interior not later than 5 days after the date on which the permit or plan is submitted;\n**(2)**\neach lessee, designee of a lessee, or applicable State shall notify the Secretary of the Interior of the approved State permit to drill or drilling plan not later than 45 days after the date on which the permit or plan is approved; and\n**(3)**\neach lessee or designee of a lessee shall provide, prior to commencing drilling operations, agreements authorizing the Secretary of the Interior to enter non-Federal land, as necessary, for inspection and enforcement of the terms of the Federal lease.\n##### (c) Nonapplicability to Indian lands\nSubsection (a) shall not apply to Indian lands (as defined in section 3 of the Federal Oil and Gas Royalty Management Act of 1982 ( 30 U.S.C. 1702 )).\n##### (d) Effect\nNothing in this section affects\u2014\n**(1)**\nother authorities of the Secretary of the Interior under the Federal Oil and Gas Royalty Management Act of 1982 ( 30 U.S.C. 1701 et seq. ); or\n**(2)**\nthe amount of royalties due to the Federal Government from the production of the Federal minerals within the oil and gas drilling or spacing unit.\n##### (e) Authority on non-Federal land\nSection 17(g) of the Mineral Leasing Act ( 30 U.S.C. 226(g) ) is amended\u2014\n**(1)**\nby striking the subsection designation and all that follows through Secretary of the Interior, or in the first sentence and inserting the following:\n(g) (1) The Secretary of the Interior, or ; and\n**(2)**\nby adding at the end the following:\n(2) (A) In the case of an oil and gas lease under this Act on land described in subparagraph (B) located within an oil and gas drilling or spacing unit, nothing in this Act authorizes the Secretary of the Interior\u2014 (i) to require a bond to protect non-Federal land; (ii) to enter non-Federal land without the consent of the applicable landowner; (iii) to impose mitigation requirements; or (iv) to require approval for surface reclamation. (B) Land referred to in subparagraph (A) is land where\u2014 (i) the Federal Government\u2014 (I) owns less than 50 percent of the minerals within the oil and gas drilling or spacing unit; and (II) does not own or lease the surface estate within the area directly impacted by the action; (ii) the well is located on non-Federal land overlying a non-Federal mineral estate, but some portion of the wellbore enters and produces from the Federal mineral estate subject to the lease; or (iii) the well is located on non-Federal land overlying a non-Federal mineral estate, but some portion of the wellbore traverses but does not produce from the Federal mineral estate subject to the lease. .",
      "versionDate": "2025-02-25",
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
        "name": "Energy",
        "updateDate": "2025-03-21T17:43:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-25",
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
          "measure-id": "id119s722",
          "measure-number": "722",
          "measure-type": "s",
          "orig-publish-date": "2025-02-25",
          "originChamber": "SENATE",
          "update-date": "2026-05-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s722v00",
            "update-date": "2026-05-04"
          },
          "action-date": "2025-02-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Bureau of Land Management Mineral Spacing Act</strong></p><p>This bill exempts certain exploration and production activities from federal\u00a0oil and gas drilling\u00a0permit requirements. Generally, the exemption applies to activities on land with (1) a surface estate that the federal government does not own, and (2) an underlying mineral estate only partially owned by the federal government. It does not apply to tribal lands.</p><p>Specifically, the bill bans the Department of the Interior from requiring a permit under the Mineral Leasing Act (MLA) when</p><ul><li>the federal government does not own or lease the surface estate, and it owns less than 50% of the mineral estate;</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore (i.e., drilled hole) enters and produces oil and gas from the federal mineral estate subject to the lease; or</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore traverses but does not produce oil or gas from the federal mineral estate subject to the lease.</li></ul><p>The bill also specifies that, in the case of an oil and gas lease on such land, the MLA does not authorize Interior to require a bond to protect nonfederal land, impose mitigation requirements, require approval for surface reclamation, or enter nonfederal land without consent of the landowner. However, lessees of federal mineral estates must authorize Interior to enter nonfederal land for inspection and enforcement of the terms of the federal lease.</p>"
        },
        "title": "Bureau of Land Management Mineral Spacing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s722.xml",
    "summary": {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Bureau of Land Management Mineral Spacing Act</strong></p><p>This bill exempts certain exploration and production activities from federal\u00a0oil and gas drilling\u00a0permit requirements. Generally, the exemption applies to activities on land with (1) a surface estate that the federal government does not own, and (2) an underlying mineral estate only partially owned by the federal government. It does not apply to tribal lands.</p><p>Specifically, the bill bans the Department of the Interior from requiring a permit under the Mineral Leasing Act (MLA) when</p><ul><li>the federal government does not own or lease the surface estate, and it owns less than 50% of the mineral estate;</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore (i.e., drilled hole) enters and produces oil and gas from the federal mineral estate subject to the lease; or</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore traverses but does not produce oil or gas from the federal mineral estate subject to the lease.</li></ul><p>The bill also specifies that, in the case of an oil and gas lease on such land, the MLA does not authorize Interior to require a bond to protect nonfederal land, impose mitigation requirements, require approval for surface reclamation, or enter nonfederal land without consent of the landowner. However, lessees of federal mineral estates must authorize Interior to enter nonfederal land for inspection and enforcement of the terms of the federal lease.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119s722"
    },
    "title": "Bureau of Land Management Mineral Spacing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Bureau of Land Management Mineral Spacing Act</strong></p><p>This bill exempts certain exploration and production activities from federal\u00a0oil and gas drilling\u00a0permit requirements. Generally, the exemption applies to activities on land with (1) a surface estate that the federal government does not own, and (2) an underlying mineral estate only partially owned by the federal government. It does not apply to tribal lands.</p><p>Specifically, the bill bans the Department of the Interior from requiring a permit under the Mineral Leasing Act (MLA) when</p><ul><li>the federal government does not own or lease the surface estate, and it owns less than 50% of the mineral estate;</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore (i.e., drilled hole) enters and produces oil and gas from the federal mineral estate subject to the lease; or</li><li>a well is located on nonfederal land overlying a nonfederal mineral estate, but some portion of the wellbore traverses but does not produce oil or gas from the federal mineral estate subject to the lease.</li></ul><p>The bill also specifies that, in the case of an oil and gas lease on such land, the MLA does not authorize Interior to require a bond to protect nonfederal land, impose mitigation requirements, require approval for surface reclamation, or enter nonfederal land without consent of the landowner. However, lessees of federal mineral estates must authorize Interior to enter nonfederal land for inspection and enforcement of the terms of the federal lease.</p>",
      "updateDate": "2026-05-04",
      "versionCode": "id119s722"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s722is.xml"
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
      "title": "Bureau of Land Management Mineral Spacing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Bureau of Land Management Mineral Spacing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to streamline the oil and gas permitting process and to recognize fee ownership for certain oil and gas drilling or spacing units, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:06Z"
    }
  ]
}
```
