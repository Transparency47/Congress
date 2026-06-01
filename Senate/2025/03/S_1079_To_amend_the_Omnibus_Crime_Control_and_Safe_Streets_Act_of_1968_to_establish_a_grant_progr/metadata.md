# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1079?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1079
- Title: Restoring Law and Order Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1079
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2025-04-09T13:26:06Z
- Update date including text: 2025-04-09T13:26:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1079",
    "number": "1079",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Restoring Law and Order Act of 2025",
    "type": "S",
    "updateDate": "2025-04-09T13:26:06Z",
    "updateDateIncludingText": "2025-04-09T13:26:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T18:30:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "TX"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "WV"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1079is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1079\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mrs. Blackburn (for herself, Mr. Hagerty , Mr. Cruz , and Mr. Justice ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program for law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Law and Order Act of 2025 .\n#### 2. Grant program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP 3061. Eligible entity defined In this part, the term eligible entity means an agency of a State, unit of local government, or Indian Tribe that is authorized by law or by an agency of a State, unit of local government, or Indian Tribe to engage in or supervise the prevention, detection, investigation, or prosecution of any violation of criminal law. 3062. Establishment of make America safe again grant program (a) In general The Attorney General shall award grants to eligible entities to\u2014 (1) hire and retain law enforcement officers, including by awarding bonuses to law enforcement officers; (2) target, combat, and prosecute vehicle thefts, including carjackings; (3) prevent violent crime by prioritizing stringent sentences for repeat offenders, including juvenile offenders; (4) use public safety tools such as bail and pretrial detention to prevent dangerous offenders from returning to communities; (5) acquire resources to better target drug and fentanyl crimes; (6) detain and deport illegal aliens who have committed criminal offenses in the United States; (7) eliminate investigatory backlogs and more quickly process criminal evidence; and (8) combat interstate child trafficking. (b) Applications An eligible entity seeking a grant under this section shall submit to the Attorney General an application at such time and in such form as the Attorney General may require. 3063. Administrative provisions (a) Regulations The Attorney General may promulgate guidelines, regulations, and procedures to carry out this part, including guidelines, regulations, and procedures relating to the submission and review of applications for grants under this part. (b) Accountability (1) Records An eligible entity that receives a grant under this part shall maintain such records as the Attorney General may require to facilitate an effective audit relating to the receipt of the grant, the use of amounts from the grant, or outsourcing activities. (2) Access For the purpose of conducting audits and examinations, the Attorney General shall have access to any book, document, or record of an eligible entity that receives a grant under this part, a State or unit of local government within which the eligible entity operates, and any entity to which the eligible entity outsources work using amounts from the grant if the Attorney General determines that the book, document, or record relates to\u2014 (A) the receipt of the grant; or (B) the use of amounts from the grant. 3064. Appropriations; funding (a) Rescission Effective on the date of enactment of the Restoring Law and Order Act of 2025 , any unobligated balances made available under section 10301(1)(A)(ii) of the Act titled An Act to provide for reconciliation pursuant to title II of S. Con. Res. 14 are rescinded. (b) Appropriation Of the unobligated balances rescinded under subsection (a)\u2014 (1) $500,000,000 is appropriated to the Attorney General for fiscal year 2026 to carry out this part, to remain available until September 30, 2030; and (2) the remainder shall be deposited in the Treasury. (c) Redirection of funds Notwithstanding any other law, the Attorney General shall use amounts appropriated to the Attorney General for the purpose of carrying out a diversity, equity, or inclusion initiative established pursuant to Executive Order 14035 ( 42 U.S.C. 2000e note; relating to diversity, equity, inclusion, and accessibility in the Federal workforce), including through the award of grants, to carry out this part. .",
      "versionDate": "2025-03-14",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-04-09T13:26:06Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1079is.xml"
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
      "title": "Restoring Law and Order Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Law and Order Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program for law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:33:14Z"
    }
  ]
}
```
