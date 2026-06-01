# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3275?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3275
- Title: Humanoid ROBOT Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3275
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-19T20:39:27Z
- Update date including text: 2025-12-19T20:39:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3275",
    "number": "3275",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Humanoid ROBOT Act of 2025",
    "type": "S",
    "updateDate": "2025-12-19T20:39:27Z",
    "updateDateIncludingText": "2025-12-19T20:39:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T20:38:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3275is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3275\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Cassidy (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo reduce the risk to the national security of the United States posed by humanoid robots produced in certain countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025 or the Humanoid ROBOT Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Country of concern**\nThe term country of concern has the meaning given the term covered nation in section 4872 of title 10, United States Code.\n**(3) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nthe government of a country of concern;\n**(B)**\na political party of a country of concern;\n**(C)**\na foreign entity of concern (as defined in section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651 ));\n**(D)**\nan entity identified by the Secretary of Defense under section 1260H(a) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note) as a Chinese military company operating directly or indirectly in the United States;\n**(E)**\nan entity with its headquarters located in, organized under the laws of, or otherwise subject to the jurisdiction of, a country of concern; or\n**(F)**\nan entity owned or controlled by, or under common ownership or control with, an entity described in any of subparagraphs (A) through (E).\n**(4) Executive agency**\nThe term executive agency has the meaning given that term in section 133 of title 41, United States Code.\n**(5) Humanoid robot**\nThe term humanoid robot means an autonomous or semi-autonomous machine that\u2014\n**(A)**\nuses integrated artificial intelligence systems;\n**(B)**\npossesses a body structure that simulates the human form, including a head, torso, arms, and legs, or any configuration that resembles a human silhouette;\n**(C)**\nis capable of performing tasks associated with human activities; and\n**(D)**\ncan communicate interactively, using natural language processing to understand verbal or written commands.\n#### 3. Prohibitions on Government contracting relating to humanoid robots from covered entities\n##### (a) Prohibition on purchases by executive agencies\nThe head of an executive agency may not enter into or renew a contract to procure or otherwise obtain a humanoid robot designed, tested, developed, or manufactured by a covered entity.\n##### (b) Prohibition on use by contractors\nA person awarded a contract by an executive agency may not use a humanoid robot designed, tested, developed, or manufactured by a covered entity to fulfill, execute, or otherwise support carrying out the contract.\n##### (c) Waiver\nThe Secretary of Defense may waive a prohibition under subsection (a) or (b) with respect to the purchase or use of a humanoid robot if using the robot is required for the completion of objectives related to national security or for research purposes.\n##### (d) Effective date\nThe prohibitions under subsections (a) and (b) shall apply on and after the date that is180 days after the date of the enactment of this Act.\n##### (e) Regulations\nNot later than 180 days after the date of the enactment of this Act, the Federal Acquisition Regulatory Council shall amend the Federal Acquisition Regulation to implement the prohibitions under subsections (a) and (b), including by establishing a requirement for prime contractors to incorporate the substance of such prohibitions and applicable implementing contract clauses into contracts relating to humanoid robots.\n#### 4. Review by Committee on Foreign Investment in the United States of investments in production of humanoid robot technologies\n##### (a) In general\nSection 721(a)(4) of the Defense Production Act of 1950 ( 50 U.S.C. 4565(a)(4) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (i), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(iii) any transaction described in subparagraph (B)(vi) proposed or pending on or after the date of the enactment of the Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025 . ;\n**(2)**\nin subparagraph (B), by adding at the end the following:\n(vi) Any other investment, subject to regulations prescribed under subparagraph (D)\u2014 (I) in a United States business that designs, tests, develops, or manufactures humanoid robots (as defined in section 2 of the Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025 ); (II) by\u2014 (aa) an entity organized under the laws of, or otherwise subject to the jurisdiction of, a covered nation (as defined in section 4872 of title 10, United States Code); or (bb) an entity owned or controlled by, or under common ownership or control with, an entity described in item (aa); and (III) without regard to whether the investment results in control of the United States business by an entity described in subclause (II). ; and\n**(3)**\nin subparagraph (D)\u2014\n**(A)**\nin clause (i), in the matter preceding subclause (I)\u2014\n**(i)**\nby striking subparagraph (B)(iii) and inserting clauses (iii) and (vi) of subparagraph (B) ; and\n**(ii)**\nby striking that subparagraph and inserting that clause ;\n**(B)**\nin clause (iii)(I), by striking subparagraph (B)(iii) and inserting clauses (iii) and (vi) of subparagraph (B) ; and\n**(C)**\nin clause (iv)(I), in the matter preceding item (aa)\u2014\n**(i)**\nby striking in subparagraph (B)(iii) and inserting in clause (iii) or (vi) of subparagraph (B) ; and\n**(ii)**\nby striking of subparagraph (B)(iii) and inserting of such clauses .\n##### (b) Mandatory filing of declarations\nSection 721(b)(1)(C)(v)(IV)(bb) of the Defense Production Act of 1950 (50 U.S.C. 4565(b)(1)(C)(v)(IV)(bb)) is amended by adding at the end the following:\n(DD) Investments in humanoid robots The parties to a covered transaction described in subsection (a)(4)(B)(vi) shall submit a declaration described in subclause (I) with respect to the transaction. .\n#### 5. Report on national security threats posed by humanoid robots\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall submit to the committees specified in subsection (c) a detailed report on the threats to the national security of the United States posed by the development and use of humanoid robots for both civilian and military purposes in countries of concern.\n##### (b) Elements\nThe report required by subsection (a) shall include the following:\n**(1)**\nAn analysis of\u2014\n**(A)**\nthe economic infrastructure and manufacturing ecosystem for humanoid robots in the People's Republic of China and other countries of concern; and\n**(B)**\nmilitary-civil fusion efforts, and other efforts, of the People\u2019s Liberation Army relating to humanoid robots.\n**(2)**\nAn analysis of how the circumvention of United States export controls and the theft of intellectual property or proprietary information of United States persons has contributed or could contribute to the development of humanoid robots in countries of concern.\n**(3)**\nRecommendations to improve such export controls.\n**(4)**\nAn analysis of the privacy and data security threats relating to the use of data of United States persons obtained through humanoid robots, including\u2014\n**(A)**\nhow the data might be stored, including whether the data is stored within the humanoid robot or on cloud infrastructure; and\n**(B)**\nhow the data is accessed by the government of a country of concern.\n**(5)**\nAn analysis of the threat that data obtained through humanoid robots designed, tested, developed, or manufactured by covered entities poses with respect to economic espionage.\n**(6)**\nRecommendations for administrative and legislative action to address national security risks posed to the United States by humanoid robots designed, tested, developed, or manufactured by covered entities.\n**(7)**\nAny other information considered relevant by the Secretary.\n##### (c) Committees specified\nThe committees specified in this subsection are\u2014\n**(1)**\nthe Committee on Commerce, Science, and Transportation, the Committee on Banking, Housing, and Urban Affairs, the Committee on Armed Services of the Senate, and Select Committee on Intelligence of the Senate; and\n**(2)**\nthe Committee on Energy and Commerce, the Committee on Foreign Affairs, the Committee on Armed Services, and the Permanent Select Committee on Intelligence of the House of Representatives.\n##### (d) Form\nThe report required by subsection (a) shall be submitted in unclassified form but may include a classified annex.",
      "versionDate": "2025-11-20",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-19T20:39:27Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3275is.xml"
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
      "title": "Humanoid ROBOT Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Humanoid ROBOT Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Humanoid Robotics Oversight and Blocking of Obtainment from Totalitarians Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce the risk to the national security of the United States posed by humanoid robots produced in certain countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:59Z"
    }
  ]
}
```
