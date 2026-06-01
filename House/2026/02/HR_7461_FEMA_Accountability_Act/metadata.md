# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7461?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7461
- Title: FEMA Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 7461
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-02-19T18:46:13Z
- Update date including text: 2026-02-19T18:46:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7461",
    "number": "7461",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "FEMA Accountability Act",
    "type": "HR",
    "updateDate": "2026-02-19T18:46:13Z",
    "updateDateIncludingText": "2026-02-19T18:46:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7461ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7461\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Bell (for himself and Mr. Moskowitz ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Administrator of the Federal Emergency Management Agency to submit a monthly report on the status of all projects and activities funded through the Disaster Relief Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the FEMA Accountability Act .\n#### 2. Reporting on Disaster Relief Fund obligations and disbursements\n##### (a) Reporting\nNot later than 60 days after the date of enactment of this Act, and monthly thereafter, the Administrator of the Federal Emergency Management Agency shall submit to the appropriate committees of Congress a report on the status of all projects and activities funded through the Disaster Relief Fund.\n##### (b) Contents of report\nEach monthly report under subsection (a) shall include, with respect to the preceding month\u2014\n**(1)**\nthe total unobligated balance of the Disaster Relief Fund;\n**(2)**\nthe total amount of Disaster Relief Fund funds obligated;\n**(3)**\nthe total amount of Disaster Relief Fund funds disbursed;\n**(4)**\na breakdown by disaster declaration (major disaster or emergency), including\u2014\n**(A)**\nthe name and date of each declaration;\n**(B)**\nthe States, territories, or tribal areas affected;\n**(C)**\nthe total funds obligated to date;\n**(D)**\nthe total funds disbursed to date; and\n**(E)**\nthe percentage of obligated funds that have been disbursed;\n**(5)**\na list of all public assistance projects submitted for approval and obligation;\n**(6)**\na list of all projects that have been approved for obligation;\n**(7)**\na list of all funds for projects that have been disbursed;\n**(8)**\na list of all projects for which obligation decisions remain pending for more than 180 days; and\n**(9)**\nany funds withheld, deferred, or reprogrammed for future use, with an explanation of the reason and estimated disbursement timeline.\n##### (c) Public availability\nThe Administrator shall make each report required under this section publicly available on the website of the Federal Emergency Management Agency not later than 10 days after the submission of each report.\n##### (d) Standardization of reporting\nNot later than 90 days after the date of enactment of this Act, the Administrator shall establish a uniform reporting template for Disaster Relief Fund obligation and disbursement data, consistent with Federal open data standards, and update such data on a rolling monthly basis.\n##### (e) Definitions\nIn this Act:\n**(1) Disaster Relief Fund**\nThe term Disaster Relief Fund means the fund established under section 102(4) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122(4) ).\n**(2) Obligation**\nThe term obligation means a legally binding commitment by the Federal Emergency Management Agency to make payments under specific disaster recovery programs or projects.\n**(3) Appropriate committees of Congress**\nThe term appropriate committees of Congress means the Committees on Appropriations and Transportation and Infrastructure of the House of Representatives and the Committees on Appropriations and Homeland Security and Governmental Affairs of the Senate.",
      "versionDate": "2026-02-10",
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
        "name": "Emergency Management",
        "updateDate": "2026-02-19T18:46:13Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7461ih.xml"
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
      "title": "FEMA Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FEMA Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Administrator of the Federal Emergency Management Agency to submit a monthly report on the status of all projects and activities funded through the Disaster Relief Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:48:24Z"
    }
  ]
}
```
