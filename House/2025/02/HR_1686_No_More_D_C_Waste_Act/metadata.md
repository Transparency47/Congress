# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1686
- Title: No More D.C. Waste Act
- Congress: 119
- Bill type: HR
- Bill number: 1686
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-09-02T17:53:20Z
- Update date including text: 2025-09-02T17:53:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1686",
    "number": "1686",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "No More D.C. Waste Act",
    "type": "HR",
    "updateDate": "2025-09-02T17:53:20Z",
    "updateDateIncludingText": "2025-09-02T17:53:20Z"
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
          "date": "2025-02-27T14:02:30Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SC"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1686ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1686\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Flood (for himself and Mr. Timmons ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the continuing availability of any portion of a Federal payment to the District of Columbia for a program of District of Columbia resident tuition support for a fiscal year which remains unobligated as of the end of the fiscal year, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No More D.C. Waste Act .\n#### 2. Prohibition on continuing availability of unobligated funds appropriated for District of Columbia resident tuition support\n##### (a) Prohibition\nAny portion of a Federal payment to the District of Columbia for a fiscal year for a program of District of Columbia resident tuition support which remains unobligated as of the end of the fiscal year shall lapse and shall not be available after the fiscal year.\n##### (b) Conforming amendments to District of Columbia College Access program\n**(1) Public school program**\nSection 3(i) of the District of Columbia College Access Act of 1999 (sec. 38\u20132702(i), D.C. Official Code) is amended by striking Such funds shall remain available until expended. .\n**(2) Private school program**\nSection 5(f) of such Act (sec. 38\u20132704(f), D.C. Official Code) is amended by striking Such funds shall remain available until expended. .\n##### (c) Effective date\nThis section and the amendments made by this section shall apply with respect to funds appropriated for fiscal year 2016 or any succeeding fiscal year.\n#### 3. Annual report on use of payments\nNot later than 60 days after the end of each fiscal year for which a Federal payment is made to the District of Columbia for a program of resident tuition support (beginning with fiscal year 2026), the Chief Financial Officer of the District of Columbia shall submit a report to Congress on the use of the payment during that fiscal year, and shall include in the report the following information:\n**(1)**\nThe number of payments made on behalf of students under the program during the fiscal year.\n**(2)**\nThe average amount of financial assistance provided with each such Federal payment.\n**(3)**\nThe amount of the Federal payment which remained unobligated (if any) as of the end of the fiscal year.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T17:53:16Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-09-02T17:53:00Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-09-02T17:53:08Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-09-02T17:53:12Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-09-02T17:53:20Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2025-09-02T17:53:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T13:07:34Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1686ih.xml"
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
      "title": "No More D.C. Waste Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No More D.C. Waste Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the continuing availability of any portion of a Federal payment to the District of Columbia for a program of District of Columbia resident tuition support for a fiscal year which remains unobligated as of the end of the fiscal year, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:52Z"
    }
  ]
}
```
