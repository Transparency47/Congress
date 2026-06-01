# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1049?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1049
- Title: Preventing Child Trafficking Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1049
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-01-10T07:09:37Z
- Update date including text: 2026-01-10T07:09:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8753-8754; text: CR S8754)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:01 - Floor: Received in the House.
- 2025-12-17 10:22:06 - Floor: Held at the desk.
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-12-16 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S8753-8754; text: CR S8754)
- 2025-12-16 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-12-16 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-16 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-12-17 - Floor: Message on Senate action sent to the House.
- 2025-12-17 09:59:01 - Floor: Received in the House.
- 2025-12-17 10:22:06 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1049",
    "number": "1049",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Preventing Child Trafficking Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:09:37Z",
    "updateDateIncludingText": "2026-01-10T07:09:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-17",
      "actionTime": "10:22:06",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-17",
      "actionTime": "09:59:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S8753-8754; text: CR S8754)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
        "item": [
          {
            "date": "2025-12-16T17:13:06Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-03-13T19:31:12Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1049is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1049\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Ossoff (for himself and Mr. Grassley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo direct the Office for Victims of Crime of the Department of Justice to continue implementing the anti-trafficking recommendations of the Government Accountability Office and to report to Congress regarding such implementation.\n#### 1. Short title\nThis Act may be cited as the Preventing Child Trafficking Act of 2025 .\n#### 2. Defined term\nIn this Act, the term anti-trafficking recommendations means the recommendations set forth in the report of the Government Accountability Office entitled Child Trafficking: Addressing Challenges to Public Awareness and Survivor Support , which was published on December 11, 2023.\n#### 3. Continued implementation of anti-trafficking programs for children\n##### (a) In general\nThe Office for Victims of Crime of the Department of Justice, in coordination with the Office on Trafficking in Persons of the Administration for Children and Families, shall continue implementing the anti-trafficking recommendations by\u2014\n**(1)**\nworking together, in accordance with the leading collaboration practices referenced in GAO\u201324-106038, to develop and implement strategies to prevent child trafficking and support child trafficking survivors; and\n**(2)**\nestablishing achievable performance goals and targets for anti-trafficking programs for children that reflect leading practices, such as being objective, measurable, and quantifiable, using baseline data from program grantees.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office for Victims of Crime shall submit a report to the Committee on the Judiciary of the Senate and Committee on the Judiciary of the House of Representatives that explicitly describes the steps taken pursuant to subsection (a).",
      "versionDate": "2025-03-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1049es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 1049\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo direct the Office for Victims of Crime of the Department of Justice to continue implementing the anti-trafficking recommendations of the Government Accountability Office and to report to Congress regarding such implementation.\n#### 1. Short title\nThis Act may be cited as the Preventing Child Trafficking Act of 2025 .\n#### 2. Defined term\nIn this Act, the term anti-trafficking recommendations means the recommendations set forth in the report of the Government Accountability Office entitled Child Trafficking: Addressing Challenges to Public Awareness and Survivor Support , which was published on December 11, 2023.\n#### 3. Continued implementation of anti-trafficking programs for children\n##### (a) In general\nThe Office for Victims of Crime of the Department of Justice, in coordination with the Office on Trafficking in Persons of the Administration for Children and Families, shall continue implementing the anti-trafficking recommendations by\u2014\n**(1)**\nworking together, in accordance with the leading collaboration practices referenced in GAO\u201324\u2013106038, to develop and implement strategies to prevent child trafficking and support child trafficking survivors; and\n**(2)**\nestablishing achievable performance goals and targets for anti-trafficking programs for children that reflect leading practices, such as being objective, measurable, and quantifiable, using baseline data from program grantees.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office for Victims of Crime shall submit a report to the Committee on the Judiciary of the Senate and Committee on the Judiciary of the House of Representatives that explicitly describes the steps taken pursuant to subsection (a).",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-12-04",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6475",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventing Child Trafficking Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child safety and welfare",
            "updateDate": "2025-12-17T19:21:43Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-17T19:21:10Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2025-12-17T19:21:39Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2025-12-17T19:21:29Z"
          },
          {
            "name": "Crimes against children",
            "updateDate": "2025-12-17T19:21:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-17T19:21:34Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-12-17T19:21:19Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-12-17T19:21:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-04T13:51:40Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1049is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1049es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Preventing Child Trafficking Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T12:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Preventing Child Trafficking Act of 2025",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Child Trafficking Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Office for Victims of Crime of the Department of Justice to continue implementing the anti-trafficking recommendations of the Government Accountability Office and to report to Congress regarding such implementation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:29Z"
    }
  ]
}
```
