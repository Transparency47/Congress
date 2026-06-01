# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/500?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/500
- Title: Amending the Rules of the House of Representatives to require employees of the House to be subject to criminal background checks conducted by the United States Capitol Police, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 500
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-09-22T15:31:09Z
- Update date including text: 2025-09-22T15:31:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House
- Latest action: 2025-06-11: Submitted in House

## Actions

- 2025-06-11 - IntroReferral: Referred to the House Committee on Rules.
- 2025-06-11 - IntroReferral: Submitted in House
- 2025-06-11 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/500",
    "number": "500",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Amending the Rules of the House of Representatives to require employees of the House to be subject to criminal background checks conducted by the United States Capitol Police, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-09-22T15:31:09Z",
    "updateDateIncludingText": "2025-09-22T15:31:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-11T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "AK"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "FL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres500ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 500\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mrs. Cammack submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to require employees of the House to be subject to criminal background checks conducted by the United States Capitol Police, and for other purposes.\n#### 1. Background checks for House employees\n##### (a) Requirement\nRule XXV of the Rules of the House of Representatives is amended by adding at the end the following new clause:\n9. (a) During each Congress, an employee of the House shall undergo a criminal background check conducted by the United States Capitol Police\u2014 (1) in the case of an employee who is employed by an office of the House on the first day of the Congress, not later than 30 days after the first day of the Congress; and (2) in the case of an employee who begins service as an employee of the House after the first day of the Congress, not later than 30 days after the employee begins service. (b) The results of a criminal background check conducted under this clause shall not be disclosed to any person other than the head of the office in which the employee is employed. (c) The Chief Administrative Officer shall enter into such agreements with the United States Capitol Police as the Chief Administrative Officer determines to be appropriate to carry out this clause. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply with respect to the One Hundred Nineteenth Congress and each succeeding Congress.\n#### 2. Report on payments from foreign governments\n##### (a) Report\nRule XXV of the Rules of the House of Representatives, as amended by section 1, is amended by adding at the end the following new clause:\n10. (a) (1) If an employee of the House received any payment from, or entered into any contract or agreement with, a government of a foreign country during the 3-year period preceding the date on which the employee begins service as an employee of the House, the employee shall file with the Clerk a report containing a description of the payment, contract, or agreement, including the identification of such government. (2) If an employee of the House is a citizen or national of a foreign country, the employee shall file with the Clerk a statement describing the employee\u2019s status as such a citizen or national, including the identification of the foreign country. (b) An individual who is required to file a report under this clause shall file the report not later than 30 days after an individual begins service as an employee of the House. (c) Upon receipt of a report filed under this clause, the Clerk shall post the report on the public website of the Office of the Clerk. (d) In this clause, the term government of a foreign country has the meaning given such term in section 1(e) of the Foreign Agent Registration Act of 1938, as Amended ( 22 U.S.C. 611(e) ). .\n##### (b) Requirement for current employees\nAn individual serving as an employee of the House of Representatives on the date of the adoption of this resolution who is required to file a report with the Clerk of the House under clause 10 of rule XXV of the Rules of the House of Representatives, as added by subsection (a), shall file the report not later than 30 days after the date of the adoption of this resolution.",
      "versionDate": "2025-06-11",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2025-06-26T14:45:19Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres500ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Amending the Rules of the House of Representatives to require employees of the House to be subject to criminal background checks conducted by the United States Capitol Police, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T08:18:28Z"
    },
    {
      "title": "Amending the Rules of the House of Representatives to require employees of the House to be subject to criminal background checks conducted by the United States Capitol Police, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T08:07:04Z"
    }
  ]
}
```
