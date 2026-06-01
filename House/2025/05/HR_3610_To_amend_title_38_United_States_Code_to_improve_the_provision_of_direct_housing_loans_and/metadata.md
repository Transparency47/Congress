# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3610
- Title: Parity for Native Hawaiian Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3610
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-12-12T09:07:27Z
- Update date including text: 2025-12-12T09:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3610",
    "number": "3610",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Parity for Native Hawaiian Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:27Z",
    "updateDateIncludingText": "2025-12-12T09:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:43:10Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3610ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3610\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Ms. Tokuda (for herself and Mr. Case ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to improve the provision of direct housing loans and medical care from the Department of Veterans Affairs for Native Hawaiians.\n#### 1. Short title\nThis Act may be cited as the Parity for Native Hawaiian Veterans Act of 2025 .\n#### 2. Modification to program for direct housing loans made to Native American veterans by the Secretary of Veterans Affairs\nSection 3765(3)(B) of title 38, United States Code, is amended by striking as that term and all that follows through 42 Stat. 108) and inserting as defined in section 801 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4221 ) .\n#### 3. Improvement of provision of medical care from Department of Veterans Affairs for Native Hawaiians\n##### (a) Reimbursement of costs of certain care provided through Native Hawaiian health care system\n**(1) In general**\nSubchapter I of chapter 17 of title 38, United States Code, is amended by inserting after section 1703G the following new section:\n1703H. Reimbursement of costs of certain care provided through Native Hawaiian health care system (a) In general The Secretary shall reimburse a Native Hawaiian health care system for the costs of care or services provided through such system to veterans eligible for such care or services under the laws administered by the Secretary, regardless of whether such care or services are provided directly through such system, through purchased or referred care, or through a contract for travel. (b) Native Hawaiian health care system defined The term Native Hawaiian health care system has the meaning given that term in section 12 of the Native Hawaiian Health Care Improvement Act ( 42 U.S.C. 11711 ). .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 1703G the following new item:\n1703H. Reimbursement of costs of certain care provided through Native Hawaiian health care system. .\n##### (b) Exemption from cost sharing\nSection 1730A(b) of such title is amended\u2014\n**(1)**\nin paragraph (1), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following new paragraph:\n(3) is a Native Hawaiian (as defined in section 12 of the Native Hawaiian Health Care Improvement Act ( 42 U.S.C. 11711 )). .",
      "versionDate": "2025-05-23",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-21",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "1853",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Parity for Native Hawaiian Veterans Act of 2025",
      "type": "S"
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
        "name": "Native Americans",
        "updateDate": "2025-06-03T18:32:49Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3610ih.xml"
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
      "title": "Parity for Native Hawaiian Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parity for Native Hawaiian Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to improve the provision of direct housing loans and medical care from the Department of Veterans Affairs for Native Hawaiians.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:21Z"
    }
  ]
}
```
