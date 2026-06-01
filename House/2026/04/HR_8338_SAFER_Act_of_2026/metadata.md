# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8338?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8338
- Title: SAFER Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8338
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-24T19:51:20Z
- Update date including text: 2026-04-24T19:51:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8338",
    "number": "8338",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "SAFER Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-24T19:51:20Z",
    "updateDateIncludingText": "2026-04-24T19:51:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8338ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8338\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Liccardo (for himself and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prevent the premature seizure of an individual\u2019s securities, digital assets, or investment accounts in the custody of a financial institution under State escheatment laws, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Americans\u2019 Fairly Earned Retirement Act of 2026 or the SAFER Act of 2026 .\n#### 2. Escheatment of certain securities, digital assets, or investment accounts held by custodians\n##### (a) In general\nWith respect to any covered asset that is directly held or beneficially owned by a person or entity and custodied by a financial institution, the financial institution may not yield custody of the covered asset, any proceeds from the sale of the covered asset, or a payment related to the covered asset (such as a dividend, principal payment, fork, or airdrop) pursuant to a State unclaimed property law, regulation, or administrative action or other means of escheatment, unless\u2014\n**(1)**\nin the case of a covered asset directly held or beneficially owned by a natural person\u2014\n**(A)**\nthe financial institution receives confirmation of the natural person\u2019s death at least 3 years before yielding custody;\n**(B)**\nno fiduciary appointed to represent the estate of the natural person has made an expression of interest in such asset, proceeds, or payment for at least 3 years before yielding custody; and\n**(C)**\nin the case of an asset, proceeds, or a payment where another natural person has an ownership interest, the financial institution receives confirmation of the other natural persons\u2019s death; or\n**(2)**\nin the case of a covered asset directly held or beneficially owned by a person or entity other than a natural person, the financial institution has no record of contact with a representative of the person or entity for at least 5 years.\n##### (b) Checking of certain inactive accounts\n**(1) In general**\nIn the case of a covered asset described in subsection (a) that is directly held or beneficially owned by a natural person who has attained retirement age and custodied by a financial institution, at the end of the 5-year period beginning on the date that the financial institution last has a record of contact with the natural person (or a representative thereof), and every five years thereafter, the financial institution shall conduct a comparison of its records with a State or Federal Government database of deaths to identify whether the natural person is deceased.\n**(2) Retirement age defined**\nIn this subsection and with respect to a natural person, the term retirement age means the applicable age, as defined in section 401(a)(9)(C)(v) of the Internal Revenue Code of 1986.\n##### (c) Death determination\nFor purposes of this section, a financial institution may confirm the death of a natural person if\u2014\n**(1)**\nthe financial institution obtains a death certificate for the natural person; or\n**(2)**\nthe financial institution obtains such other legal documents as the institution determines sufficient to confirm the death of the natural person.\n##### (d) Preemption\nThis section preempts any State law, regulation, ordinance, or other provision that requires a financial institution to remit, escheat, yield custody, or otherwise transfer any asset, security, or investment account to a State or local government in any manner that conflicts with this section.\n##### (e) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthis section does not preempt any State law, regulation, ordinance, or other provision requiring communication between the State and a financial institution or a person or entity that directly holds or beneficially owns a covered asset; and\n**(2)**\nthis section does not prevent an owner of a covered asset from seeking remedies through State or Federal law for mishandling or improper escheatment of a covered asset.\n##### (f) Definitions\nIn this section:\n**(1) Covered asset**\nThe term covered asset \u2014\n**(A)**\nmeans any\u2014\n**(i)**\nsecurity;\n**(ii)**\ndigital asset; or\n**(iii)**\ninvestment account; and\n**(B)**\ndoes not include an employee benefit plan subject to title I of the Employee Retirement Income Security Act of 1974.\n**(2) Digital asset**\nThe term digital asset means any digital representation of value which is recorded on a cryptographically-secured distributed ledger or other similar technology.\n**(3) Employee benefit plan**\nThe term employee benefit plan has the meaning given that term under section 3(3) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1002(3) ).\n**(4) Financial institution**\nThe term financial institution \u2014\n**(A)**\nhas the meaning given that term under section 5312 of title 31, United States Code; and\n**(B)**\nincludes any\u2014\n**(i)**\nnational bank;\n**(ii)**\ntransfer agent; or\n**(iii)**\ncentralized digital asset exchange.\n**(5) Investment account**\nThe term investment account means an account, including a retirement account, that can be used to hold, manage, buy, sell, or trade a digital asset or security.\n**(6) Security**\nThe term security has the meaning given that term under section 3 of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c ).\n**(7) State**\nThe term State means each of the several States, the District of Columbia, and each territory or possession of the United States.\n##### (g) Rule of application\nThis section shall apply to a covered asset, proceeds from the sale of a covered asset, and a payment related to a covered asset\u2014\n**(1)**\nthat is held or beneficially owned by a person or entity on or after the date of enactment of this Act; and\n**(2)**\nthe custody of which has not been yielded pursuant to a State unclaimed property law, regulation, or administrative action or other means of escheatment as of the date of enactment of this Act.",
      "versionDate": "2026-04-16",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-24T19:51:19Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8338ih.xml"
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
      "title": "SAFER Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFER Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Americans\u2019 Fairly Earned Retirement Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T03:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent the premature seizure of an individual's securities, digital assets, or investment accounts in the custody of a financial institution under State escheatment laws, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T03:33:26Z"
    }
  ]
}
```
