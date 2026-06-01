# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1760?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1760
- Title: USPS Act
- Congress: 119
- Bill type: HR
- Bill number: 1760
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-05-08T13:45:15Z
- Update date including text: 2025-05-08T13:45:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1760",
    "number": "1760",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000814",
        "district": "14",
        "firstName": "Randy",
        "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
        "lastName": "Weber",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "USPS Act",
    "type": "HR",
    "updateDate": "2025-05-08T13:45:15Z",
    "updateDateIncludingText": "2025-05-08T13:45:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:03:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1760ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1760\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Weber of Texas introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Comptroller General of the United States to submit reports to Congress on theft of mail and United States Postal Service property and other civil or criminal violations relating to the Postal Service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upholding a Secure Postal System Act or the USPS Act .\n#### 2. Reports on mail and Postal Service property theft\n##### (a) In general\nNot later than 1 year after the date of the enactment of this section and each year thereafter for 5 years, the Comptroller General of the United States shall investigate nationwide patterns and instances of the theft of mail, delays of mail, United States Postal Service employee violations investigated by the Office of the Inspector General of the Postal Service, any other criminal or civil violations under the jurisdiction of the Postal Inspection Service, and the theft or vandalism of Postal Service property, and submit a report on each such investigation to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate.\n##### (b) Contents\nAny report under subsection (a) shall include a description of any measures the Postal Service has in place to address violations described under such subsection and recommendations on how the Postal Service and Congress can combat such violations.\n##### (c) Consultation\nIn carrying out this section, the Comptroller General shall consult with the Inspector General of the Postal Service and the Postal Inspection Service.",
      "versionDate": "2025-02-27",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-08T13:45:15Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1760ih.xml"
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
      "title": "USPS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USPS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Upholding a Secure Postal System Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to submit reports to Congress on theft of mail and United States Postal Service property and other civil or criminal violations relating to the Postal Service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:50Z"
    }
  ]
}
```
