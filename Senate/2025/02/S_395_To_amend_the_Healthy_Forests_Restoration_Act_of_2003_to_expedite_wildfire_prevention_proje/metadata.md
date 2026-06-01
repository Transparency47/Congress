# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/395?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/395
- Title: Emergency Fuel Reduction Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 395
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-12-31T17:36:55Z
- Update date including text: 2025-12-31T17:36:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/395",
    "number": "395",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Emergency Fuel Reduction Act of 2025",
    "type": "S",
    "updateDate": "2025-12-31T17:36:55Z",
    "updateDateIncludingText": "2025-12-31T17:36:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T20:00:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sponsorshipDate": "2025-02-04",
      "state": "WY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s395is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 395\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Ms. Lummis (for herself, Mr. Barrasso , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend the Healthy Forests Restoration Act of 2003 to expedite wildfire prevention projects to reduce the risk of wildfire on certain high-risk Federal land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Fuel Reduction Act of 2025 .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto expedite wildfire prevention projects to reduce the risk of wildfire on certain high-risk Federal land adjacent to communities, private property, and critical infrastructure;\n**(2)**\nto improve forest and wildland health; and\n**(3)**\nto promote the recovery of threatened or endangered species or other species under consideration to be listed under the Endangered Species Act of 1973 ( 16 U.S.C. 1531 et seq. ), including the sage-grouse species, the habitat of which is negatively impacted by wildland fire.\n#### 3. Expedited review of projects on Federal land\nSection 104 of the Healthy Forests Restoration Act of 2003 ( 16 U.S.C. 6514 ) is amended\u2014\n**(1)**\nby redesignating subsections (e) through (h) as subsections (f) through (i), respectively;\n**(2)**\nin subsection (c)(1)(C)(i), by striking subsection (f) and inserting subsection (g) ; and\n**(3)**\nby inserting after subsection (d) the following:\n(e) Categorical exclusion of certain projects (1) In general An authorized hazardous fuel reduction project shall be categorically excluded from the requirements of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4321 et seq. ) if the authorized hazardous fuel reduction project\u2014 (A) involves the removal of\u2014 (i) insect-infected trees; (ii) dead or dying trees; (iii) trees presenting a threat to public safety; or (iv) other hazardous fuels threatening\u2014 (I) utility or communications infrastructure; (II) municipal water supply systems; (III) campgrounds; (IV) roadsides; (V) schools; or (VI) other infrastructure; (B) is conducted on Federal land on which the Secretary determines that conditions, such as the risk of wildfire, an insect or disease epidemic, or the presence of invasive species, pose a risk to adjacent non-Federal land; or (C) treats 10,000 acres or less of Federal land that\u2014 (i) is at particular risk for wildfire; (ii) contains threatened and endangered species habitat; or (iii) provides conservation benefits to\u2014 (I) a species that is not listed as an endangered species or a threatened species under section 4 of the Endangered Species Act of 1973 ( 16 U.S.C. 1533 ), but is under consideration to be so listed; (II) a State-listed species; or (III) a special concern species. (2) Applicability This subsection shall not apply to Federal land\u2014 (A) that is a component of the National Wilderness Preservation System; (B) on which the removal of vegetation is specifically prohibited by Federal law; or (C) that is within a National Monument as of the date of enactment of the Emergency Fuel Reduction Act of 2025 . .",
      "versionDate": "2025-02-04",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Endangered and threatened species",
            "updateDate": "2025-09-10T18:09:55Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2025-09-10T18:09:55Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-09-10T18:09:55Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-10T18:09:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-07T19:39:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119s395",
          "measure-number": "395",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-12-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s395v00",
            "update-date": "2025-12-31"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Emergency Fuel Reduction Act of 2025</strong></p><p>This bill categorically excludes from the environmental review\u00a0requirements of the National Environmental Policy Act of 1969 (NEPA) certain hazardous fuel reduction projects on federal land. A categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to a hazardous fuel reduction project that (1) involves the removal of trees that are dead, dying, or insect-infected or present a threat to public safety; (2) involves the removal of hazardous fuels threatening infrastructure; (3) is conducted on federal land with conditions that pose a risk to adjacent nonfederal land; or (4)\u00a0treats 10,000 acres or less of federal land that is at particular risk for wildfire, contains threatened and endangered species habitat, or provides conservation benefits to certain species, such as\u00a0a special concern species.</p><p>This categorical exclusion does not apply to federal land (1) that is a component of the National Wilderness Preservation System, (2) on which the removal of vegetation is specifically prohibited by federal law, or (3) that is within a national monument as of the date of enactment of this bill.</p>"
        },
        "title": "Emergency Fuel Reduction Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s395.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Emergency Fuel Reduction Act of 2025</strong></p><p>This bill categorically excludes from the environmental review\u00a0requirements of the National Environmental Policy Act of 1969 (NEPA) certain hazardous fuel reduction projects on federal land. A categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to a hazardous fuel reduction project that (1) involves the removal of trees that are dead, dying, or insect-infected or present a threat to public safety; (2) involves the removal of hazardous fuels threatening infrastructure; (3) is conducted on federal land with conditions that pose a risk to adjacent nonfederal land; or (4)\u00a0treats 10,000 acres or less of federal land that is at particular risk for wildfire, contains threatened and endangered species habitat, or provides conservation benefits to certain species, such as\u00a0a special concern species.</p><p>This categorical exclusion does not apply to federal land (1) that is a component of the National Wilderness Preservation System, (2) on which the removal of vegetation is specifically prohibited by federal law, or (3) that is within a national monument as of the date of enactment of this bill.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119s395"
    },
    "title": "Emergency Fuel Reduction Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Emergency Fuel Reduction Act of 2025</strong></p><p>This bill categorically excludes from the environmental review\u00a0requirements of the National Environmental Policy Act of 1969 (NEPA) certain hazardous fuel reduction projects on federal land. A categorical exclusion applies to a class of actions that do not require an environmental assessment nor an environmental impact statement under NEPA.</p><p>The categorical exclusion established by the bill applies to a hazardous fuel reduction project that (1) involves the removal of trees that are dead, dying, or insect-infected or present a threat to public safety; (2) involves the removal of hazardous fuels threatening infrastructure; (3) is conducted on federal land with conditions that pose a risk to adjacent nonfederal land; or (4)\u00a0treats 10,000 acres or less of federal land that is at particular risk for wildfire, contains threatened and endangered species habitat, or provides conservation benefits to certain species, such as\u00a0a special concern species.</p><p>This categorical exclusion does not apply to federal land (1) that is a component of the National Wilderness Preservation System, (2) on which the removal of vegetation is specifically prohibited by federal law, or (3) that is within a national monument as of the date of enactment of this bill.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119s395"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s395is.xml"
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
      "title": "Emergency Fuel Reduction Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T02:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Emergency Fuel Reduction Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T02:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Healthy Forests Restoration Act of 2003 to expedite wildfire prevention projects to reduce the risk of wildfire on certain high-risk Federal land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T02:48:26Z"
    }
  ]
}
```
