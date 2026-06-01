# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/20?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/20
- Title: Establishing the Congressional Fitness Challenge, and for other purposes.
- Congress: 119
- Bill type: HCONRES
- Bill number: 20
- Origin chamber: House
- Introduced date: 2025-03-24
- Update date: 2025-06-05T08:07:02Z
- Update date including text: 2025-06-05T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-24: Introduced in House
- 2025-03-24 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-24 - IntroReferral: Submitted in House
- 2025-03-24 - IntroReferral: Submitted in House
- Latest action: 2025-03-24: Submitted in House

## Actions

- 2025-03-24 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-03-24 - IntroReferral: Submitted in House
- 2025-03-24 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/20",
    "number": "20",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Establishing the Congressional Fitness Challenge, and for other purposes.",
    "type": "HCONRES",
    "updateDate": "2025-06-05T08:07:02Z",
    "updateDateIncludingText": "2025-06-05T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-24",
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
          "date": "2025-03-24T16:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "GA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MP"
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
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "WI"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "AK"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres20ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 20\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2025 Mr. Hamadeh of Arizona submitted the following concurrent resolution; which was referred to the Committee on House Administration\nCONCURRENT RESOLUTION\nEstablishing the Congressional Fitness Challenge, and for other purposes.\n#### 1. Congressional Fitness Challenge\nThere is established a national recognition program, to be known as the Congressional Fitness Challenge (in this concurrent resolution referred to as the Challenge ), to promote physical fitness and personal achievement among eligible participants through voluntary, performance-based fitness tests.\n#### 2. Tests\nThe Challenge shall be comprised of the following tests to be administered to eligible participants:\n**(1)**\n1-mile run or walk, which shall be assessed based on the time taken to run or walk 1 mile.\n**(2)**\nPull-ups or flexed arm hang, which shall be assessed based on the maximum number of continuous pull-ups or flexed arm hangs completed with proper form.\n**(3)**\nCurl-ups or sit-ups, which shall be assessed based on the number of curl-ups or sit-ups completed in 60 seconds.\n**(4)**\nShuttle run, which shall be assessed based on the time taken to run 30 feet back and forth between 2 parallel lines, picking up a block of wood or similar object twice at 1 such line, for a total of 120 feet.\n**(5)**\nSit-and-reach, which shall be assessed based on the maximum distance reached.\n#### 3. Administration of Challenge\n##### (a) Challenge sponsors\nThe following entities may sponsor the Challenge:\n**(1)**\nA public or private school that provides education in any grade from kindergarten through grade 12.\n**(2)**\nA Member of the House of Representatives or Senator who organizes a community-based event.\n**(3)**\nAn independent entity that provides testing for an eligible participant that attends a home school.\n##### (b) Test administrators\nThe tests under section 2 shall be administered by a certified fitness professional.\n#### 4. Benchmarks\n##### (a) In general\nThe covered committees shall consult with fitness organizations or certified fitness professionals to finalize and publish benchmarks that set a performance standard for each test under section 2 based on age and gender. In finalizing such benchmarks, such committees shall take into account the historical standards used in the Presidential Physical Fitness Test.\n##### (b) Adaptive standards\nSuch benchmarks shall include adaptive standards for eligible participants with disabilities.\n#### 5. Data collection\n##### (a) In general\nAn entity sponsoring the Challenge under section 3(a) shall submit to the covered committees the data of all eligible participants who participate in the Challenge sponsored by such entity.\n##### (b) Data aggregation\nThe covered committees shall aggregate such data based on the gender and age group of such participants across the United States for each 1-year period.\n#### 6. Recognition\n##### (a) In general\nAn eligible participant who performs at or above the benchmarks under section 4 in the gender and age group of such participant for each test under section 2 may receive a certificate that is signed by\u2014\n**(1)**\nthe Speaker of the House of Representatives;\n**(2)**\nthe President pro tempore of the Senate;\n**(3)**\nthe Member of the House of Representatives who represents the congressional district in which such participant resides; and\n**(4)**\nthe Senator of the State in which such participant resides.\n##### (b) Recognition levels\nFor an eligible participant who performs at or above the following percentiles in the gender and age group of such participant for each test under section 2, a certificate under subsection (a) shall indicate the lowest recognition level achieved on any such test as follows:\n**(1)**\nGold level: Top 85th percentile of eligible participants who participated in the Challenge.\n**(2)**\nSilver level: Top 75th percentile of eligible participants who participated in the Challenge.\n**(3)**\nBronze level: Top 50th percentile of eligible participants who participated in the Challenge.\n#### 7. Administration and oversight\n##### (a) Regulations and guidance\nThe covered committees shall jointly\u2014\n**(1)**\nprescribe regulations to oversee the Challenge, including\u2014\n**(A)**\ntesting protocols;\n**(B)**\nmechanisms to report any information needed for recognition under section 6 to the Member of the House of Representatives who represents the congressional district in which an eligible participant resides and the Senator of the State in which such participant resides;\n**(C)**\nregulations to protect the privacy of eligible participants who participate in the Challenge and address the liability risks of sponsors under section 3(a); and\n**(D)**\nuniform standards for submitting data to the covered committees under section 5; and\n**(2)**\nissue guidance on the use of\u2014\n**(A)**\na Members\u2019 Representational Allowance by a Member of the House of Representatives under subsection (b); and\n**(B)**\na Senators\u2019 Official Personnel and Office Expense Account by a Senator under subsection (b).\n##### (b) Funding sources\n**(1) In general**\n**(A) Members\u2019 Representational Allowance**\nA Member of the House of Representatives may use amounts provided under the Members\u2019 Representational Allowance of such Member under section 101 of the House of Representatives Administrative Reform Technical Corrections Act ( 2 U.S.C. 5341 ) to carry out activities related to the Challenge.\n**(B) Senators\u2019 Official Personnel and Office Expense Account**\nA Senator may use amounts provided under the Senators\u2019 Official Personnel and Office Expense Account of such Senator under the first section of Public Law 100\u2013137 ( 2 U.S.C. 6313 ) to carry out activities related to the Challenge.\n**(2) Alternative funding**\nNot later than 1 year after the date of enactment of this Act, the Subcommittees on the Legislative Branch of the Committees on Appropriations of the House of Representatives and the Senate shall publish a report on the feasibility and desirability of using other funds of the House of Representatives and Senate in covering expenses incurred in carrying out the Challenge.\n#### 8. Definitions\nIn this concurrent resolution:\n**(1) Certified fitness professional**\nThe term certified fitness professional means a fitness professional with a relevant certification, as determined by a sponsor under section 3(a), such as\u2014\n**(A)**\na physical education teacher at a public or private school that provides education in a grade from kindergarten through grade 12, but only with respect to eligible participants who are in an age group for which such teacher is qualified to administer the tests under section 2; or\n**(B)**\na physical trainer with a certification from the National Academy of Sports Medicine, the American Council on Exercise, or a similar entity.\n**(2) Covered committees**\nThe term covered committees means the Committee on House Administration of the House of Representatives and the Committee on Rules and Administration of the Senate.\n**(3) Eligible participant**\nThe term eligible participant means a student, including a student attending a public, private, or home school, aged 6 through 17.\n**(4) Member of the House of Representatives**\nThe term Member of the House of Representatives means a Representative in, or a Delegate or Resident Commissioner to, the Congress.",
      "versionDate": "2025-03-24",
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
        "updateDate": "2025-03-26T12:48:04Z"
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
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres20ih.xml"
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
      "title": "Establishing the Congressional Fitness Challenge, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T08:18:30Z"
    },
    {
      "title": "Establishing the Congressional Fitness Challenge, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T08:06:07Z"
    }
  ]
}
```
