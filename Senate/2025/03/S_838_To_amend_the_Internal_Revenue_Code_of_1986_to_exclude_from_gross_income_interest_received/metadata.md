# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/838?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/838
- Title: ACRE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 838
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2025-12-05T21:40:24Z
- Update date including text: 2025-12-05T21:40:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/838",
    "number": "838",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "ACRE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:40:24Z",
    "updateDateIncludingText": "2025-12-05T21:40:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T20:32:12Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-04",
      "state": "ME"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "AL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "ND"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "KS"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "DE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s838is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 838\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mr. Moran (for himself, Mr. King , Mr. Tuberville , Mr. Gallego , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income interest received on certain loans secured by rural or agricultural real property.\n#### 1. Short title\nThis Act may be cited as the Access to Credit for our Rural Economy Act of 2025 or as the ACRE Act of 2025 .\n#### 2. Exclusion of interest on loans secured by rural or agricultural real property\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Interest on loans secured by rural or agricultural real property (a) In general Gross income shall not include interest received by a qualified lender on any qualified real estate loan. (b) Qualified lender For purposes of this section, the term qualified lender means\u2014 (1) any bank or savings association the deposits of which are insured under the Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ), (2) any State- or federally regulated insurance company, (3) any entity wholly owned, directly or indirectly, by a company that is treated as a bank holding company for purposes of section 8 of the International Banking Act of 1978 ( 12 U.S.C. 3106 ) if\u2014 (A) such entity is organized, incorporated, or established under the laws of the United States or any State of the United States, and (B) the principal place of business of such entity is in the United States (including any territory of the United States), (4) any entity wholly owned, directly or indirectly, by a company that is considered an insurance holding company under the laws of any State if such entity satisfies the requirements described in subparagraphs (A) and (B) of paragraph (3), and (5) with respect to interest received on a qualified real estate loan secured by real estate described in subsection (c)(3)(A), any federally chartered instrumentality of the United States established under section 8.1(a) of the Farm Credit Act of 1971 ( 12 U.S.C. 2279aa\u20131(a) ). (c) Qualified real estate loan For purposes of this section\u2014 (1) In general The term qualified real estate loan means any loan\u2014 (A) secured by\u2014 (i) rural or agricultural real estate or forestland, or (ii) a leasehold mortgage (with a status as a lien) on rural or agricultural real estate, (B) which is made to a person other than a foreign adversary entity, (C) in the case of any loan with respect to single family residence described in paragraph (3)(B)\u2014 (i) the proceeds of which are used to purchase or improve such residence, and (ii) the principal of which (when added to the principal of all other such loans with respect to such residence) does not (as of the time the interest income on such loan is accrued) exceed $750,000, and (D) made after the date of the enactment of this section. For purposes of the preceding sentence, the determination of whether property securing such loan is rural or agricultural real estate shall be made as of the time the interest income on such loan is accrued. (2) Refinancings For purposes of subparagraphs (A) and (C) of paragraph (1), a loan shall not be treated as made after the date of the enactment of this section to the extent that the proceeds of such loan are used to refinance a loan which was made on or before the date of the enactment of this Act (or, in the case of any series of refinancings, the original loan was made on or before such date). (3) Rural or agricultural real estate The term rural or agricultural real estate means\u2014 (A) any real property which is substantially used for the production of one or more agricultural products, (B) any single family residence\u2014 (i) which is the principal residence (within the meaning of section 121) of its occupant, and (ii) which is located in a rural area within the meaning of section 1.11(b)(3) of the Agricultural Credit Act of 1987 ( 12 U.S.C. 2019(b)(3) ), (C) any real property which is substantially used in the trade or business of fishing or seafood processing, and (D) any aquaculture facility. (4) Aquaculture facility The term aquaculture facility means any land, structure, or other appurtenance that is used for aquaculture (including any hatchery, rearing pond, raceway, pen, or incubator) that is located in any State or any territory of the United States. (5) Foreign adversary entity (A) In general The term foreign adversary entity means\u2014 (i) a foreign adversary, (ii) a foreign person subject to the jurisdiction of, or organized under the laws of, a foreign adversary, and (iii) a foreign person owned, directed, or controlled by an entity described in clause (i) or (ii). (B) Foreign adversary The term foreign adversary means\u2014 (i) the People\u2019s Republic of China, including all Special Administrative Regions, (ii) the Republic of Cuba, (iii) the Islamic Republic of Iran, (iv) the Democratic People\u2019s Republic of Korea, (v) the Russian Federation, and (vi) the Bolivarian Republic of Venezuela during any period of time in which Nichol\u00e1s Maduro is President of the Republic. (d) Coordination with section 265 Qualified real estate loans shall be treated as obligations described in section 265(a)(2) the interest on which is wholly exempt from the taxes imposed by this subtitle. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Interest on loans secured by rural or agricultural real property. .\n##### (c) Report to Congress\nNot later than 5 years after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall submit a written report to the Committee on Ways and Means of House of Representatives and the Committee on Finance of the Senate analyzing the impact of section 139J of the Internal Revenue Code of 1986 (as added by subsection (a)) on qualified real estate loans (as defined in such section), including whether such section has resulted in a reduction in the rate of interest on such loans.\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-03-04",
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
        "actionDate": "2025-03-04",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1822",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ACRE Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-05-08T19:38:03Z"
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
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s838is.xml"
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
      "title": "ACRE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACRE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Access to Credit for our Rural Economy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude from gross income interest received on certain loans secured by rural or agricultural real property.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:31Z"
    }
  ]
}
```
