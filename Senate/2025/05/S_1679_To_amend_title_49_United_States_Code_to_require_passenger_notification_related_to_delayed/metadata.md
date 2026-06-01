# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1679?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1679
- Title: FLIGHT Act
- Congress: 119
- Bill type: S
- Bill number: 1679
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-05T22:57:17Z
- Update date including text: 2025-12-05T22:57:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1679",
    "number": "1679",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FLIGHT Act",
    "type": "S",
    "updateDate": "2025-12-05T22:57:17Z",
    "updateDateIncludingText": "2025-12-05T22:57:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T16:59:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1679is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1679\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo amend title 49, United States Code, to require passenger notification related to delayed flights, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Frequent Logistics Information for Grounded and Held Travelers Act or the FLIGHT Act .\n#### 2. Passenger notification of delayed flights\n##### (a) In general\nChapter 423 of title 49, United States Code, is amended by inserting after section 42308 the following:\n42309. Passenger notification of delayed flights (a) In general In the case of a domestic or international flight operated by a covered air carrier (as such term is defined in section 42307) that is experiencing a delayed departure or taxi delay of 15 or more minutes, the covered air carrier shall notify each passenger on the flight of the delay in accordance with the requirements of in subsection (b). (b) Requirements With respect to a notification under subsection (a), the requirements described in this subsection are the following: (1) The notification shall occur not less frequently than once every 15 minutes until the delayed departure or taxi delay concludes. (2) The notification shall be provided to each passenger by email or text message. (3) The notification shall include\u2014 (A) information regarding the new estimated time of departure and arrival, as applicable to the delayed departure or taxi delay; and (B) a mechanism for the passenger to opt out of receiving such notifications with respect to such flight. .\n##### (b) Clerical amendment\nThe analysis for chapter 423 of title 49, United States Code, is amended by inserting after the item relating to section 42308 the following:\n42309. Passenger notification of delayed flights. .",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-09-03",
        "text": "Referred to the Subcommittee on Aviation."
      },
      "number": "5087",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FLIGHT Act",
      "type": "HR"
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
        "updateDate": "2025-05-23T14:26:07Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1679is.xml"
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
      "title": "FLIGHT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FLIGHT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Frequent Logistics Information for Grounded and Held Travelers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 49, United States Code, to require passenger notification related to delayed flights, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:18Z"
    }
  ]
}
```
