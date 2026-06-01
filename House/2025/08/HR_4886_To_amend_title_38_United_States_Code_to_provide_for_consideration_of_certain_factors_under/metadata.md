# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4886
- Title: Larry Barrett Veterans’ Memory Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4886
- Origin chamber: House
- Introduced date: 2025-08-05
- Update date: 2025-12-20T09:06:53Z
- Update date including text: 2025-12-20T09:06:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-05: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-08-05: Introduced in House

## Actions

- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Introduced in House
- 2025-08-05 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-05",
    "latestAction": {
      "actionDate": "2025-08-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4886",
    "number": "4886",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Larry Barrett Veterans\u2019 Memory Care Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:53Z",
    "updateDateIncludingText": "2025-12-20T09:06:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
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
      "actionDate": "2025-08-05",
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
      "actionDate": "2025-08-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-05",
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
          "date": "2025-08-05T14:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:11:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4886\nIN THE HOUSE OF REPRESENTATIVES\nAugust 5, 2025 Mrs. Houchin introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for consideration of certain factors under the Veterans Community Care Program, to provide for expedited approval of certain requests for Veterans Care Agreements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Larry Barrett Veterans\u2019 Memory Care Act of 2025 .\n#### 2. Consideration under Veterans Community Care Program of veteran preference for care, continuity of care, and need for caregiver or attendant\n##### (a) In general\nSection 1703(d)(2) of title 38, United States Code, is amended by adding at the end the following new subparagraphs:\n(F) During the three-year period beginning on the date of the enactment of the Dignity in Veterans Aging Act of 2025\u2014 (i) in the case of a covered veteran seeking extended care services\u2014 (I) the preference of the covered veteran for where, when, and how to seek such services; and (II) whether the covered veteran requests or requires the assistance of a caregiver or attendant when seeking such services; and (ii) continuity of care. .\n##### (b) Treatment of sunset\nIn the case of a veteran who is a covered veteran under section 1703 of title 38, United States Code, and who is receiving extended care services pursuant to subparagraph (F) of subsection (d)(2) of such section, the veteran may continue to receive such care or services until the end of the episode of care notwithstanding the termination date specified in such subparagraph.\n#### 3. Expedited approval process for certain requests for Veterans Care Agreements\nSection 1703A of title 38, United States Code, is amended\u2014\n**(1)**\nby redesignating subsections (k) and (l) as subsections (l) and (m), respectively;\n**(2)**\nby inserting after subsection (j) the following new subsection (k):\n(k) Expedited approval process (1) In the case of a request made by a covered individual described in paragraph (2) for a Veterans Care Agreement with an eligible entity or provider, the Secretary shall\u2014 (A) approve the request under this section, including the certification under subsection (c) regardless of whether the eligible entity or provider meets the criteria under such subsection or the requirements under subsection (e), by not later than 30 days after the date on which the request is made; and (B) during the period beginning on the date of the request and ending on the date of the approval of the request, provide in-home care services for the covered veteran under section 1720L of this title. (2) A covered individual described in this subsection is a covered individual who\u2014 (A) has expressed to the Secretary a preference to receive an extended care service required by the individual from an eligible entity or provider that\u2014 (i) is not party to a Veterans Care Agreement under this section; and (ii) is not a health care provider specified in section 1703(c) of this title; and (B) resides in a location that requires traveling for longer than an hour to reach the location of any health care provider specified in section 1703(c) of this title who is qualified to furnish the extended care service required by the individual. ; and\n**(3)**\nin subsection (e)(1), by striking subsection (k) and inserting subsection (l) .",
      "versionDate": "2025-08-05",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-05T15:28:57Z"
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
      "date": "2025-08-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4886ih.xml"
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
      "title": "Larry Barrett Veterans\u2019 Memory Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T10:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Larry Barrett Veterans\u2019 Memory Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T10:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for consideration of certain factors under the Veterans Community Care Program, to provide for expedited approval of certain requests for Veterans Care Agreements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T10:18:19Z"
    }
  ]
}
```
