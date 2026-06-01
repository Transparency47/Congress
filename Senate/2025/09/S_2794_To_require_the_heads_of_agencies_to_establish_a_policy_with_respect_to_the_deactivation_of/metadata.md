# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2794
- Title: DECLINE Act
- Congress: 119
- Bill type: S
- Bill number: 2794
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-30T11:03:16Z
- Update date including text: 2025-09-30T11:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2794",
    "number": "2794",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "DECLINE Act",
    "type": "S",
    "updateDate": "2025-09-30T11:03:16Z",
    "updateDateIncludingText": "2025-09-30T11:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T21:38:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "TN"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2794is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2794\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Ms. Ernst (for herself, Mrs. Blackburn , and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo require the heads of agencies to establish a policy with respect to the deactivation of charge cards of employees separating from the agency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Deactivating and Eliminating Cards Linked to Inactive or Nonexistent Employees Act or the DECLINE Act .\n#### 2. Deactivation of charge cards upon employee separation\n##### (a) Definitions\nIn this section:\n**(1) Agency**\nThe term agency has the meaning given the term in section 5701 of title 5, United States Code.\n**(2) Charge card**\nThe term charge card means a purchase card, travel card, or other form of Federal Government payment card\u2014\n**(A)**\nissued by an agency; and\n**(B)**\nassigned to an employee of an agency.\n**(3) Covered individual**\nThe term covered individual \u2014\n**(A)**\nmeans an individual who is discharged, separates, retires, or otherwise ceases employment with an agency; and\n**(B)**\nincludes an individual who, before the discharge, separation, or cease of employment described in subparagraph (A), held\u2014\n**(i)**\na position described in section 5312, 5313, 5314, or 5315 of title 5, United States Code;\n**(ii)**\na noncareer Senior Executive Service position, as defined in section 3132(a) of title 5, United States Code; and\n**(iii)**\na position in the executive branch of a confidential or policy-determining character described in schedule C of subpart C of part 213 of title 5, Code of Federal Regulations.\n##### (b) Policy\nNot later than 30 days after the date of enactment of this Act, the chief financial officer or the functional equivalent officer of each agency, in consultation with the chief human capital officer or the functional equivalent of each agency, shall establish and implement a policy requiring that, as part of the official separation process from the agency of a covered individual and with respect to any charge card assigned to the covered individual\u2014\n**(1)**\nthe covered individual returns the charge card to the agency;\n**(2)**\npersonnel of the agency physically secure the charge card;\n**(3)**\nthe covered individual remove the charge card from any digital wallet or electronic device owned by the covered individual or issued to the covered individual in connection with the employment of the covered individual at the agency;\n**(4)**\nappropriate agency personnel immediately deactivate the charge card and close or suspend the account associated with the charge card in accordance with agency procedures; and\n**(5)**\nappropriate agency personnel report the charge card to the issuing financial institution as no longer valid for use or reissuance in connection with the covered individual.\n##### (c) GAO review of agency compliance\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Comptroller General of the United States shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report that includes\u2014\n**(1)**\nthe number of charge cards issued and deactivated by each agency;\n**(2)**\nthe extent to which agencies have established internal controls to monitor charge card use and address misuse, fraud, or redundant card issuance;\n**(3)**\nthe status of the implementation of subsection (b) by each agency;\n**(4)**\nthe total amount each agency paid in charge card late fees during the preceding 1-year period; and\n**(5)**\nthe extent to which agencies submit required management reports through the electronic access system of the bank with which the agency has a contract, including a summary of the report data of selected agencies, such as account activity, disputes, and unusual spending patterns.",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-26T15:29:34Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2794is.xml"
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
      "title": "DECLINE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DECLINE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Deactivating and Eliminating Cards Linked to Inactive or Nonexistent Employees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the heads of agencies to establish a policy with respect to the deactivation of charge cards of employees separating from the agency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:18Z"
    }
  ]
}
```
