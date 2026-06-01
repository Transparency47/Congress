# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2952?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2952
- Title: SALT Act
- Congress: 119
- Bill type: HR
- Bill number: 2952
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2952",
    "number": "2952",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "O000086",
        "district": "4",
        "firstName": "Burgess",
        "fullName": "Rep. Owens, Burgess [R-UT-4]",
        "lastName": "Owens",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "SALT Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:32:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-04-29",
      "state": "TX"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2952ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2952\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Owens introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Labor-Management Reporting and Disclosure Act of 1959 to clarify reporting requirements.\n#### 1. Short title\nThis Act may be cited as the Start Applying Labor Transparency Act or SALT Act .\n#### 2. Labor-Management Reporting and Disclosure Act of 1959\n##### (a) Filing and contents of report of payments, loans, promises, agreements, or arrangements\nSection 201 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 431 ) is amended\u2014\n**(1)**\nby redesignating subsections (c) through (e) as subsections (d) through (f), respectively; and\n**(2)**\nby inserting after subsection (b) the following:\n(c) Every labor organization who in any fiscal year made\u2014 (1) any payment or loan, direct or indirect, of money or any other thing of value (including reimbursed expenses), or any promise or agreement therefor, to an employee, or a group or committee of employees, of an employer (other than the labor organization) for the purpose of causing such employee or group or committee to persuade other employees to exercise or not to exercise, or as the manner of exercising, the right to organize and bargain collectively through representatives of their own choosing unless such payments were contemporaneously or previously disclosed to such other employees; (2) any agreement or arrangement with a labor relations consultant or other independent contractor or organization pursuant to which such consultant, independent contractor, or organization undertakes activities where an object thereof, directly or indirectly, is to persuade employees to exercise or not to exercise, or persuade employees as to the manner of exercising, the right to organize and bargain collectively through representatives of their own choosing, or undertakes to supply such labor organization with information concerning the activities of employees or an employer in connection with a labor dispute involving such labor organization, except information for use solely in conjunction with an administrative or arbitral proceeding or a criminal or civil judicial proceeding; or (3) any payment (including reimbursed expenses) pursuant to an agreement or arrangement described in paragraph (2); shall file with the Secretary a report, in a form prescribed by the Secretary, signed by its treasurer or corresponding principal officers showing in detail the date and amount of each such payment, loan, promise, agreement, or arrangement and the name, address, and position, if any, of any firm or person to whom it was made and a full explanation of the circumstances of all such payments, including the terms of any agreement or understanding pursuant to which they were made. This shall include the name of any employer targeted by such individual and the location of the employer\u2019s targeted facility. .\n##### (b) Persuasive activities relating to the right To organize and bargain collectively; supplying information of activities in connection with labor disputes; filing and contents of report of agreement or arrangement\n**(1) In general**\nSection 202 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 432 ) is amended\u2014\n**(A)**\nby redesignating subsection (c) as subsection (d); and\n**(B)**\nby inserting after subsection (b) the following:\n(c) Every person who receives payment or loan, direct or indirect, of money or any other thing of value (including reimbursed expenses), or any promise or agreement therefor from another to seek employment with a third party where an object thereof is in whole or in part, directly or indirectly\u2014 (1) persuade employees of the third party to exercise or not to exercise, or as to the manner of exercising, the right to organize and bargain collectively through representatives of their own choosing; or (2) supply a labor organization with information concerning the activities of employees or agents of third party in connection with a labor dispute involving such third part, except information for use solely in conjunction with an administrative or arbitral proceeding or a criminal or civil judicial proceeding; shall file within thirty days after entering into such agreement or arrangement a report with the Secretary, signed by its treasurer or corresponding principal officers, containing the name under which such person is engaged in doing business and the address of its principal office, and a detailed statement of the terms and conditions of such agreement or arrangement. Every such person shall file annually, with respect to each fiscal year during which payments were made as a result of such an agreement or arrangement, a report with the Secretary, signed by its president and treasurer or corresponding principal officers, containing a statement (A) of its receipts of any kind from labor organizations on account of labor relations advice or services, designating the sources thereof, and (B) of its disbursements of any kind, in connection with such services and the purposes thereof. In each such case such information shall be set forth in such categories as the Secretary may prescribe. .\n**(2) Conforming amendment**\nSection 202 of the Labor-Management Reporting and Disclosure Act of 1959 ( 29 U.S.C. 432 ) is amended in subsection (d), as redesignated by paragraph (1), by striking under subsection (a) and inserting under subsection (a) or (c) .\n#### 3. Regulations\nNot later than 6 months after the date of enactment of this Act, the Secretary of Labor shall issue such regulations as are necessary to carry out the amendments made by this Act.",
      "versionDate": "2025-04-17",
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
        "name": "Labor and Employment",
        "updateDate": "2025-05-20T14:07:40Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2952ih.xml"
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
      "title": "SALT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SALT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Start Applying Labor Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Labor-Management Reporting and Disclosure Act of 1959 to clarify reporting requirements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:48:31Z"
    }
  ]
}
```
