# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5823
- Title: Watershed Protection and Forest Recovery Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5823
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5823",
    "number": "5823",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Watershed Protection and Forest Recovery Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-10-24T18:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "UT"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5823ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5823\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Mr. Neguse (for himself and Ms. Maloy ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Credit Act of 1978 to authorize the Secretary of Agriculture to carry out emergency watershed protection measures on National Forest System land, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Watershed Protection and Forest Recovery Act of 2025 .\n#### 2. Emergency forest watershed program\n##### (a) Funding and administration\nSection 404(b) of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2204(b) ) is amended by inserting to carry out section 401 after for a fiscal year .\n##### (b) Emergency forest watershed program\nTitle IV of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2201 et seq. ) is amended by adding at the end the following:\n408. Emergency forest watershed program (a) Definitions In this section: (1) Emergency watershed protection measures The term emergency watershed protection measures means measures that\u2014 (A) are necessary to address runoff retardation, soil-erosion prevention, and flood mitigation caused by a natural disaster or any other natural occurrence that has caused a sudden impairment to natural resources on National Forest System land, and the damage, if not treated\u2014 (i) would significantly impair or endanger the natural resources on the National Forest System land; and (ii) would pose an immediate risk to water resources or loss of life or property downstream of the National Forest System land; and (B) would maintain or restore forest health and forest-related resources on the National Forest System land. (2) Natural disaster The term natural disaster has the meaning given the term in section 407(a). (3) Secretary The term Secretary means the Secretary, acting through the Chief of the Forest Service. (4) Sponsor The term sponsor means\u2014 (A) a State or local government; (B) an Indian Tribe (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); and (C) a water district, water conservation district, water utility, or special district. (b) Authorization The Secretary, acting through a sponsor, is authorized to undertake emergency watershed protection measures on National Forest System land. (c) Agreements; payments (1) In general The Secretary may enter into an agreement with a sponsor and make payments to the sponsor, on request of the sponsor, to carry out emergency watershed protection measures. (2) Requirements (A) Project timelines (i) In general Following a natural disaster or natural occurrence that necessitates the carrying out of emergency watershed protection measures, the Secretary shall execute agreements under paragraph (1) as expeditiously as possible. (ii) Timeline A sponsor that has entered into an agreement under paragraph (1) shall complete all emergency watershed protection measures not later than 2 years after the conclusion of the applicable natural disaster or natural occurrence, as determined by the Secretary, that necessitated the carrying out of those measures. (iii) Continued monitoring A sponsor that has entered into an agreement under paragraph (1) may monitor, maintain, repair, or replace emergency watershed protection measures for a period of not more than 3 years following the conclusion of the natural disaster or natural occurrence, as determined by the Secretary, that necessitated the carrying out of those measures when failure to do so would result in unacceptable risk to National Forest System land or downstream water users. (B) Payments The Secretary, in accordance with an agreement entered into under paragraph (1)\u2014 (i) may make partial payments prior to completion of the applicable project; and (ii) shall make final payment for the project not later than 30 days after the date on which the project is completed. (d) Waived matching requirements The Secretary shall waive any matching requirements for payments made under subsection (c)(1). (e) Liability (1) In general A sponsor that carries out emergency watershed protection measures pursuant to an agreement under subsection (c)(1) shall not\u2014 (A) be required to indemnify the United States for any liability resulting from carrying out emergency watershed protection measures pursuant to that agreement; or (B) except as provided in paragraph (2), be liable for injury, loss, or damage resulting from carrying out emergency watershed protection measures pursuant to that agreement. (2) Savings provision Nothing in this subsection precludes liability for damages or costs relating to the carrying out of emergency watershed protection measures by a sponsor pursuant to an agreement entered into under subsection (c)(1) if the sponsor acted with willful or wanton negligence or reckless conduct in carrying out those measures. (f) Assumption of risk A sponsor that carries out emergency watershed protection measures prior to entering into an agreement under subsection (c)(1) shall assume the risk of incurring any cost or liability resulting from carrying out those measures. (g) Coordination The Chief of the Natural Resources Conservation Service shall coordinate on the use of funds distributed under this section and section 403. (h) NEPA compliance Emergency watershed protection measures carried out pursuant to this section shall be deemed emergency response actions for purposes of section 220.4(b)(1) of title 36, Code of Federal Regulations (or a successor regulation). .",
      "versionDate": "2025-10-24",
      "versionType": "Introduced in House"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-08T21:21:09Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5823ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Watershed Protection and Forest Recovery Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Watershed Protection and Forest Recovery Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Agricultural Credit Act of 1978 to authorize the Secretary of Agriculture to carry out emergency watershed protection measures on National Forest System land, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T10:03:14Z"
    }
  ]
}
```
