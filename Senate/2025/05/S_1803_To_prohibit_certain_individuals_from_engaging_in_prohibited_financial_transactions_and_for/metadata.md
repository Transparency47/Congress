# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1803?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1803
- Title: STABLE GENIUS Act
- Congress: 119
- Bill type: S
- Bill number: 1803
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2026-01-10T07:33:22Z
- Update date including text: 2026-01-10T07:33:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1803",
    "number": "1803",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "STABLE GENIUS Act",
    "type": "S",
    "updateDate": "2026-01-10T07:33:22Z",
    "updateDateIncludingText": "2026-01-10T07:33:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T21:05:48Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1803is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1803\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Bennet introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo prohibit certain individuals from engaging in prohibited financial transactions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Trading Assets Benefitting Lawmakers' Earnings while Governing Exotic and Novel Investments in the United States Act or the STABLE GENIUS Act .\n#### 2. Prohibited financial transactions\n##### (a) Definitions\nIn this section:\n**(1) Covered election**\nThe term covered election means an election for the office of\u2014\n**(A)**\nPresident;\n**(B)**\nVice President;\n**(C)**\nUnited States Senator;\n**(D)**\nUnited States Representative;\n**(E)**\nDelegate to Congress; or\n**(F)**\nResident Commissioner of Puerto Rico.\n**(2) Covered individual**\nThe term covered individual means\u2014\n**(A)**\nthe President;\n**(B)**\nthe Vice President;\n**(C)**\na United States Senator;\n**(D)**\na United States Representative;\n**(E)**\na Delegate to Congress;\n**(F)**\na Resident Commissioner of Puerto Rico; or\n**(G)**\na candidate in a covered election.\n**(3) Covered investment**\nThe term covered investment means any digital asset.\n**(4) Digital asset**\nThe term digital asset means any digital representation of value that is recorded on a cryptographically secured distributed ledger or any similar technology.\n**(5) Prohibited financial transaction**\n**(A) In general**\nThe term prohibited financial transaction means\u2014\n**(i)**\nany issuance, sponsorship, or endorsement of a covered investment;\n**(ii)**\nany purchase, sale, holding, or other conduct that causes a covered individual to obtain a covered investment;\n**(iii)**\nany acquisition of any financial interest comparable to an interest described in clause (i) or (ii) through synthetic means, such as the use of a derivative, including an option, warrant, or other similar means; or\n**(iv)**\nany acquisition of any financial interest comparable to an interest described in clause (i) or (ii) as part of an aggregation or compilation of such interests through a mutual fund, exchange-traded fund, or other similar means.\n**(6) Qualified blind trust**\nThe term qualified blind trust means a qualified blind trust (as defined in section 13104(f)(3) of title 5, United States Code) that has been approved in writing by the applicable supervising ethics office under subparagraph (D) of such section 13104(f)(3).\n##### (b) Prohibited financial transactions\nExcept as provided in subsection (c), a covered individual may not engage in any prohibited financial transaction during\u2014\n**(1)**\nthe period beginning on the date of filing as a candidate in a covered Federal election and ending on the date of the covered Federal election;\n**(2)**\nthe term of service of the covered individual; and\n**(3)**\nthe 1-year period beginning on the date on which the service of the covered individual is terminated.\n##### (c) Qualified blind trust\n**(1) In general**\nDuring any of the periods described in subsection (b), for each covered investment owned by a covered individual, the covered individual shall place the covered investment in a qualified blind trust, including by establishing a qualified blind trust for that purpose, if necessary.\n**(2) Qualified blind trust requirements**\nA qualified blind trust may not be established for purposes of complying with this section without the prior approval of the applicable supervising ethics office. With respect to any such trust so approved, the applicable trustee\u2014\n**(A)**\nshall divest of any such instrument placed in the trust not later than 6 months after the trust is established;\n**(B)**\nshall certify to the applicable supervising ethics office on an annual basis that the trustee has not provided any information on the trust\u2019s assets or transactions to the applicable covered individual; and\n**(C)**\nmay not have a close personal or business relationship with the applicable covered individual.\n##### (d) Reporting requirements\n**(1) Supervising ethics offices**\nEach supervising ethics office shall make available on the public website of the supervising ethics office a copy of any qualified blind trust agreement of each covered individual.\n**(2) Amendment**\nSection 13101(18) of title 5, United States Code, is amended\u2014\n**(A)**\nin subparagraph (C), by striking and at the end;\n**(B)**\nin subparagraph (D), by striking the period and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(E) the Federal Election Commission for a candidate in an election for the office of President, Vice President, United States Senator, United States Representative, Delegate to Congress, or Resident Commissioner of Puerto Rico. .\n##### (e) Liability and immunity\nFor purposes of any immunities to civil or criminal liability, any conduct comprising or relating to a prohibited financial transaction under this section shall be deemed an unofficial act and beyond the scope of the official duties of the relevant covered individual.\n##### (f) Civil penalties\n**(1) Civil action**\nThe Attorney General may bring a civil action in any appropriate district court of the United States against any covered individual who violates subsection (b).\n**(2) Civil penalty**\nAny covered individual who knowingly violates subsection (b) shall be subject to a civil monetary penalty of not more than $250,000.\n**(3) Disgorgement**\nA covered individual who is found in a civil action under paragraph (1) to have violated subsection (b) shall disgorge to the Treasury of the United States any profit from the unlawful activity that is the subject of that civil action.\n##### (g) Criminal penalties\n**(1) In general**\nIt shall be unlawful for a covered individual to\u2014\n**(A)**\nknowingly violate subsection (b); and\n**(B)**\nthrough such violation\u2014\n**(i)**\ncauses an aggregate loss of not less than $1,000,000 to 1 or more persons in the United States; or\n**(ii)**\nbenefits financially, through profit, gain, or advantage, directly or indirectly through any family member or business associate of the covered individual, from a prohibited financial transaction.\n**(2) Penalty**\nA covered individual who violates paragraph (1) shall be fined under title 18, United States Code, imprisoned for not more than 18 years, or both.",
      "versionDate": "2025-05-19",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-09",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committees on Oversight and Government Reform, and House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3849",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STABLE GENIUS Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-23T17:11:12Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1803is.xml"
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
      "title": "STABLE GENIUS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STABLE GENIUS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Trading Assets Benefitting Lawmakers' Earnings while Governing Exotic and Novel Investments in the United States Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit certain individuals from engaging in prohibited financial transactions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:30Z"
    }
  ]
}
```
