# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8288
- Title: Strengthening Export Controls Compliance Act
- Congress: 119
- Bill type: HR
- Bill number: 8288
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-22T14:20:26Z
- Update date including text: 2026-05-22T14:20:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 39 - 5.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 39 - 5.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8288",
    "number": "8288",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "A000380",
        "district": "1",
        "firstName": "Gabe",
        "fullName": "Rep. Amo, Gabe [D-RI-1]",
        "lastName": "Amo",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Strengthening Export Controls Compliance Act",
    "type": "HR",
    "updateDate": "2026-05-22T14:20:26Z",
    "updateDateIncludingText": "2026-05-22T14:20:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 39 - 5.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
        "item": [
          {
            "date": "2026-04-22T20:12:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:01:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "IN"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8288ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8288\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Amo (for himself and Mr. Shreve ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo amend the Export Control Reform Act of 2018 to provide assistance for compliance with that Act.\n#### 1. Short title\nThis Act may be cited as the Strengthening Export Controls Compliance Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Export Control Reform Act of 2018 calls on the Secretary of Commerce to establish a system to provide United States persons with assistance in complying with United States export controls as well as keep the public appropriately apprised of changes in policy, regulations, and procedures established under that Act.\n**(2)**\nThe Export Control Reform Act of 2018 also calls on the Secretary of Commerce to report annually to Congress on efforts to provide exporters with compliance assistance, including specific actions to assist small- and medium-sized businesses .\n**(3)**\nThe Bureau of Industry and Security also generally holds an annual update conference on export controls to increase the public\u2019s and industry\u2019s understanding of United States export controls policies, as well as provide compliance guidance and regulatory updates.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is critical for the national security and technological leadership of the United States that the Bureau of Industry and Security of the Department of Commerce consistently inform and educate United States businesses on evolving export control regulations and their implementation; and\n**(2)**\nseminars and trainings offered by the Bureau of Industry and Security can serve as a valuable resource for United States businesses, especially small- and medium-sized enterprises, that do not have large compliance departments.\n#### 4. Compliance assistance\nSection 1757 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4816 ) is amended by striking subsection (c) and inserting the following:\n(c) Assistance for U.S. industry (1) Industry Outreach Plan Every two years, the President shall develop and submit to Congress a plan to assist United States persons, especially small- and medium-sized United States businesses, in export licensing and other processes under this part. The plan should include the following: (A) Arrangements for the Department of Commerce to provide counseling to United States persons on filing applications and related submissions, including identifying items controlled under this part. (B) Proposals for virtual and in-person trainings, seminars, and conferences to educate United States businesses on export controls, Bureau of Industry and Security licensing procedures, and related obligations. (C) Other activities to facilitate compliance by United States businesses, including review of company compliance plans, follow-up on license conditions, and company specific consultations on specific issues. (2) Annual conference The Secretary shall host an annual conference, to be known as the Update Conference on Export Controls and Policy , to provide compliance assistance and policy updates to industry and other stakeholders. The conference should be listed on the Bureau of Industry and Security\u2019s website and open to anyone from the general public. (3) Compliance assistance for new rules Prior to the promulgation of major new rules to carry out this part, the Bureau of Industry and Security shall carry out dedicated public and industry outreach to share details with respect to the intent and implementation of the rule, with the goal of strengthening compliance. .\n#### 5. Amendments to the annual report\nSection 1765(a) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4824(a) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking a review of ;\n**(2)**\nin paragraph (4), insert a detailed list of before efforts ;\n**(3)**\nin paragraph (8), strike and at the end;\n**(4)**\nin paragraph (9), by striking the period at the end and inserting ; and ; and\n**(5)**\nby adding at the end the following:\n(10) information on the number of Advisory Opinion and Commodity Classification requests, including\u2014 (A) the number of requests submitted; (B) the number of Advisory Opinion or Commodity Classifications issued as a result of the requests submitted under subparagraph (A); (C) the average processing times for each category of request; and (D) the number of redacted Advisory Opinions of general applicability posted. .",
      "versionDate": "2026-04-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:34:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-01T18:35:03Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:35:08Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:35:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-20T23:16:36Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8288ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Export Controls Compliance Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "title": "Strengthening Export Controls Compliance Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Export Control Reform Act of 2018 to provide assistance for compliance with that Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T12:33:43Z"
    }
  ]
}
```
