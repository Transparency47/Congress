# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5087?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5087
- Title: FLIGHT Act
- Congress: 119
- Bill type: HR
- Bill number: 5087
- Origin chamber: House
- Introduced date: 2025-09-02
- Update date: 2025-12-05T22:53:56Z
- Update date including text: 2025-12-05T22:53:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-02: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-03 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-09-02: Introduced in House

## Actions

- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Introduced in House
- 2025-09-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-03 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-02",
    "latestAction": {
      "actionDate": "2025-09-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5087",
    "number": "5087",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FLIGHT Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:53:56Z",
    "updateDateIncludingText": "2025-12-05T22:53:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-02",
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
          "date": "2025-09-02T16:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-03T21:38:20Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5087ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5087\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 2, 2025 Ms. Lee of Florida introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to require passenger notification related to delayed flights, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Frequent Logistics Information for Grounded and Held Travelers Act or the FLIGHT Act .\n#### 2. Passenger notification of delayed flights\n##### (a) In general\nChapter 423 of title 49, United States Code, is amended by inserting after section 42308 the following:\n42309. Passenger notification of delayed flights (a) In general In the case of a domestic or international flight operated by a covered air carrier (as such term is defined in section 42307) that is experiencing a delayed departure or taxi delay of 15 or more minutes, the covered air carrier shall notify each passenger on the flight of the delay in accordance with the requirements of in subsection (b). (b) Requirements With respect to a notification under subsection (a), the requirements described in this subsection are the following: (1) The notification shall occur not less frequently than once every 15 minutes until the delayed departure or taxi delay concludes. (2) The notification shall be provided to each passenger by email or text message. (3) The notification shall include\u2014 (A) information regarding the new estimated time of departure and arrival, as applicable to the delayed departure or taxi delay; and (B) a mechanism for the passenger to opt out of receiving such notifications with respect to such flight. .\n##### (b) Clerical amendment\nThe analysis for chapter 423 of title 49, United States Code, is amended by inserting after the item relating to section 42308 the following:\n42309. Passenger notification of delayed flights. .",
      "versionDate": "2025-09-02",
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
        "actionDate": "2025-05-08",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1679",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FLIGHT Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-22T13:56:27Z"
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
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5087ih.xml"
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
      "title": "FLIGHT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FLIGHT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Frequent Logistics Information for Grounded and Held Travelers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require passenger notification related to delayed flights, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:34Z"
    }
  ]
}
```
