# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7357
- Title: TSP Fiduciary Security Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7357
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-23T23:08:24Z
- Update date including text: 2026-02-23T23:08:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7357",
    "number": "7357",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "TSP Fiduciary Security Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-23T23:08:24Z",
    "updateDateIncludingText": "2026-02-23T23:08:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:04:35Z",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "NY"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7357ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7357\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Fine (for himself, Mr. Harrigan , and Mr. Moran ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to address the responsibilities of fiduciaries with respect to the Thrift Savings Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TSP Fiduciary Security Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Federal Retirement Thrift Investment Board has a fiduciary duty to manage the Thrift Savings Fund in the best interest of the beneficiaries of the Fund.\n**(2)**\nThe principal beneficiaries of the Thrift Savings Fund are the civil servants of the United States, and members of the uniformed services, who are tasked with defending the national security of the United States.\n**(3)**\nThe duty of the Federal Retirement Thrift Investment Board to manage the Thrift Savings Fund in the best interests of the beneficiaries of the Fund includes a duty not to harm the national security of the United States.\n#### 3. Fiduciary responsibilities with respect to Thrift Savings Fund\nSection 8477 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (B), by striking ; and and inserting a semicolon;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(D) to the maximum extent practicable, by preventing the investments of the Thrift Savings Fund (or portions thereof), and the exercise of voting rights associated with any such investments, from harming the national security of the United States. ; and\n**(2)**\nin subsection (e), by adding at the end the following:\n(9) (A) Notwithstanding any other provision of this subsection, no fiduciary shall be personally liable for any monetary damages, or be assessed any civil penalty, under this subsection with respect to a breach of the requirement under subsection (b)(1)(D). (B) Subparagraph (A) shall cease to have effect beginning on January 1, 2027. .\n#### 4. Review of Thrift Savings Fund for compliance with fiduciary duties\n##### (a) In general\nSection 8477(f) of title 5, United States Code, is amended\u2014\n**(1)**\nby inserting (1) after (f) ; and\n**(2)**\nby adding at the end the following:\n(2) (A) Not later than 1 year after the date of enactment of this paragraph, the Secretary of Labor, in consultation with the Secretary of Defense, the Attorney General, the Secretary of Homeland Security, and the Secretary of the Treasury, shall prescribe regulations to carry out subsection (b)(1)(D) with respect to each of the following: (i) The investments of the Thrift Savings Fund, which shall include the establishment of standards by which compliance with subsection (b)(1)(D) with respect to the investments of the Thrift Savings Fund (or portions thereof) shall be determined. (ii) The exercise of voting rights associated with the investments of the Thrift Savings Fund (or portions thereof). (B) The regulations prescribed under subparagraph (A)(ii) shall include\u2014 (i) the establishment of a process by which the exercise of voting rights described in subparagraph (A)(ii) shall be reviewed by the Secretary of Labor, in consultation with the Secretary of Defense, the Attorney General, the Secretary of Homeland Security, and the Secretary of the Treasury, for compliance with subsection (b)(1)(D) with respect to the exercise of those rights; and (ii) the establishment of standards by which compliance with subsection (b)(1)(D) with respect to the exercise of voting rights described in subparagraph (A)(ii) shall be determined, including the factors contributing to a determination that a covered vote would not comply with subsection (b)(1)(D). (C) For the purposes of any regulation prescribed under subparagraph (A), the Secretary of Labor shall presume that\u2014 (i) an investment of the Thrift Savings Fund (or portions thereof) does not comply with subsection (b)(1)(D) if the investment invests in\u2014 (I) an entity included on\u2014 (aa) the list of Communist Chinese military companies maintained under section 1237(b) of the Strom Thurmond National Defense Authorization Act for Fiscal Year 1999 ( 50 U.S.C. 1701 note); or (bb) the entity list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations; or (II) a parent, subsidiary, or affiliate of, or an entity controlled by, an entity described in subclause (I); and (ii) an exercise of voting rights associated with any investments of the Thrift Savings Fund (or portions thereof) does not comply with subsection (b)(1)(D) if that exercise of voting rights is a covered vote with respect to a proposal that would\u2014 (I) approve or ratify a transaction, including a transaction described in subparagraph (D)(ii)(I), that would cause, or would reasonably be expected to cause, an entity to which the covered vote applies to\u2014 (aa) breach any contract with the Federal Government to which the entity is a party, and under which the consideration provided to the entity over the course of the entire contract is more than $10,000,000, if the entity has otherwise complied with all applicable laws and regulations in fulfilling the responsibilities of the entity with respect to the contract; (bb) significantly reduce the production of, or the capital expenditure or research and development expenditure with respect to, any\u2014 (AA) industrial resources, critical technology items, or materials that are essential to the national defense (as those terms are defined in section 702 of the Defense Production Act of 1950 ( 50 U.S.C. 4552 )); or (BB) emerging and foundational technology identified by the President under section 1758 of the Export Controls Act of 2018 ( 50 U.S.C. 4817 ); or (cc) outsource or substantially sell, whether to any affiliated entity or joint venture, or by contract, to any entity located in a covered country, any\u2014 (AA) industrial resources, critical technology items, or materials that are essential to the national defense (as those terms are defined in section 702 of the Defense Production Act of 1950 ( 50 U.S.C. 4552 )); or (BB) emerging and foundational technology identified by the President under section 1758 of the Export Controls Act of 2018 ( 50 U.S.C. 4817 ); or (II) elect to the board of directors of any entity an individual who\u2014 (aa) is a director, officer, employee, or affiliate of any entity described in clause (i)(I); (bb) at any time during the 5-year period preceding the date on which that election occurs, was as described in item (aa); or (cc) a reasonable investor would believe supports any proposal described in subclause (I). (D) In this paragraph\u2014 (i) the term covered country means\u2014 (I) the People\u2019s Republic of China, the Russian Federation, North Korea, Iran, Syria, Sudan, Venezuela, or Cuba; (II) any country, the government of which the Secretary of State determines has repeatedly provided support for acts of international terrorism pursuant to\u2014 (aa) section 1754(c)(1)(A) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A) ); (bb) section 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); (cc) section 40 of the Arms Export Control Act ( 22 U.S.C. 2780 ); or (dd) any other provision of law; or (III) any other country that the Secretary of Labor, in consultation with the Secretary of Defense, the Attorney General, the Secretary of Homeland Security, and the Secretary of the Treasury, designates as posing an undue or unnecessary risk to the national security of the United States; and (ii) the term covered vote means a vote in favor of (or an abstention with respect to) a proposal to\u2014 (I) approve or ratify a transaction involving an entity, including\u2014 (aa) any sale of, or other disposition of (whether in a single or a series of transactions) assets or capital stock; and (bb) any merger, consolidation, joint venture, partnership, spin-off, reverse spin-off, dissolution, restructuring, recapitalization, liquidation, or any other business combination or strategic transaction; or (II) elect an individual to the board of directors of the entity that is the subject of the proposal. .\n##### (b) Review of exercise of voting rights; report to Congress\nSection 8438 of title 5, United States Code, is amended\u2014\n**(1)**\nin subsection (f)\u2014\n**(A)**\nby inserting (1) after (f) ; and\n**(B)**\nby adding at the end the following:\n(2) For the purposes of paragraph (1), a review of the exercise of voting rights for compliance with section 8477(b)(1)(D), including under the regulations prescribed under section 8477(f)(2), shall not be considered to be the exercise of voting rights associated with the ownership of securities by the Thrift Savings Fund. ; and\n**(2)**\nby adding at the end the following:\n(i) Not later than 2 years after the date of enactment of this subsection, and annually thereafter, the Secretary of Labor shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report regarding\u2014 (1) for the year covered by the report, the investments of the Thrift Savings Fund (or portions thereof), and the exercise of voting rights associated with any such investments, that have been reviewed for compliance with section 8477(b)(1)(D); and (2) the outcome with respect to enforcement of each review conducted under paragraph (1) and a justification for that outcome. .\n#### 5. Prohibition on investment of Thrift Savings Fund sums in entities based in the People\u2019s Republic of China through the TSP mutual fund window\nSection 8438(b)(5) of title 5, United States Code, is amended by adding at the end the following:\n(E) A mutual fund accessible through a mutual fund window authorized under this paragraph may not include an investment in any security of\u2014 (i) an entity based in the People\u2019s Republic of China; or (ii) any subsidiary that is owned or operated by an entity described in clause (i). .",
      "versionDate": "2026-02-04",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "1368",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "TSP Fiduciary Security Act of 2025",
      "type": "S"
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
        "updateDate": "2026-02-23T23:08:23Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7357ih.xml"
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
      "title": "TSP Fiduciary Security Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TSP Fiduciary Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to address the responsibilities of fiduciaries with respect to the Thrift Savings Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:20Z"
    }
  ]
}
```
