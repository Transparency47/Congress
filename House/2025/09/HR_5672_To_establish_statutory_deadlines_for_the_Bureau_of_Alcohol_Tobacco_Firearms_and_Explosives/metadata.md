# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5672?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5672
- Title: Reducing Unnecessary Slowdowns in Handling Act
- Congress: 119
- Bill type: HR
- Bill number: 5672
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-01-21T09:05:17Z
- Update date including text: 2026-01-21T09:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5672",
    "number": "5672",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Reducing Unnecessary Slowdowns in Handling Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:17Z",
    "updateDateIncludingText": "2026-01-21T09:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "AL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "KS"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5672ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5672\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mr. Williams of Texas (for himself and Mr. Moore of Alabama ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish statutory deadlines for the Bureau of Alcohol, Tobacco, Firearms, and Explosives to process permit applications, and require quarterly congressional and public reporting on application processing metrics and compliance.\n#### 1. Short title\nThis Act may be cited as the Reducing Unnecessary Slowdowns in Handling Act .\n#### 2. Statutory processing deadlines\n##### (a) Applications to the ATF generally\nWithin 90 calendar days after receipt of an application not described in subsection (b), the Bureau shall complete processing of the application.\n##### (b) Applications relating to licenses under section 923 of title 18 , United States Code\nWithin 60 calendar days after receipt of an application relating to a license under section 923 of title 18, United States Code, the Bureau shall complete processing of the application.\n#### 3. Quarterly congressional and public reporting requirement\nWithin 90 days after the date of the enactment of this Act, and every 90 days thereafter, the Bureau shall submit to the Committees on Oversight and Accountability and on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate, and shall make available to the public on the website of the Bureau, a report that contains the following, with respect to each type of application processed during the 90-day period ending with the date the report is so submitted:\n**(1)**\nA specification of the number of applications received, approved, denied, and pending.\n**(2)**\nA specification of the length of time taken to process the applications.\n**(3)**\nA summary of reasons for delays in the processing of the applications.\n**(4)**\nA summary of reasons for denials of the applications.\n#### 4. Internal oversight and implementation\n##### (a) Appeals process\nThe Bureau shall establish a process for applicants to appeal the denial of an application, or to compel the completion of the processing of an application the processing of which is not in compliance with section 2.\n##### (b) Internal oversight\nThe Bureau shall establish procedures to identify the causes of noncompliance with section 2, and to take necessary corrective actions.\n##### (c) Implementation\nThe Bureau shall implement this Act through the use of funds otherwise made available to the Bureau for salaries and expenses, and not by hiring additional personnel or acquiring additional resources, and in doing so shall eliminate repetitive reviews and unnecessary administrative steps, and revise any outdated or duplicative procedural processes hindering the timely processing of permits.\n#### 5. Definitions\nIn this Act:\n**(1) Application**\nThe term application means an application for a license, permit, authorization, or a form required by Federal law to be submitted to the Bureau.\n**(2) Bureau**\nThe term Bureau means the Bureau of Alcohol, Tobacco, Firearms, and Explosives.\n**(3) Easily accessible format**\nThe term easily accessible format means, with respect to a report, a format that is available to the general public and allows users to efficiently locate and read the report.",
      "versionDate": "2025-09-30",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-08T18:06:30Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5672ih.xml"
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
      "title": "Reducing Unnecessary Slowdowns in Handling Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T11:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Unnecessary Slowdowns in Handling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish statutory deadlines for the Bureau of Alcohol, Tobacco, Firearms, and Explosives to process permit applications, and require quarterly congressional and public reporting on application processing metrics and compliance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:15Z"
    }
  ]
}
```
