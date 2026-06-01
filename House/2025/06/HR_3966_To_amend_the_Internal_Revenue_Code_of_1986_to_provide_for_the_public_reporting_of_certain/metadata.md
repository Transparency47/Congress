# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3966?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3966
- Title: Think Tank and Nonprofit Foreign Influence Disclosure Act
- Congress: 119
- Bill type: HR
- Bill number: 3966
- Origin chamber: House
- Introduced date: 2025-06-12
- Update date: 2025-06-30T18:05:45Z
- Update date including text: 2025-06-30T18:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-12: Introduced in House

## Actions

- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Introduced in House
- 2025-06-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3966",
    "number": "3966",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000589",
        "district": "5",
        "firstName": "Lance",
        "fullName": "Rep. Gooden, Lance [R-TX-5]",
        "lastName": "Gooden",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Think Tank and Nonprofit Foreign Influence Disclosure Act",
    "type": "HR",
    "updateDate": "2025-06-30T18:05:45Z",
    "updateDateIncludingText": "2025-06-30T18:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T14:09:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
      "state": "WI"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "MI"
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
      "sponsorshipDate": "2025-06-23",
      "state": "AK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3966ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3966\nIN THE HOUSE OF REPRESENTATIVES\nJune 12, 2025 Mr. Gooden (for himself and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for the public reporting of certain contributions received by charitable organizations from foreign governments and foreign political parties.\n#### 1. Short title\nThis Act may be cited as the Think Tank and Nonprofit Foreign Influence Disclosure Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nForeign governments and foreign political parties attempt to influence the government and political system of the United States through donations to nonprofit charitable organizations, especially think tanks and cultural organizations. While institutions of higher education are required to disclose foreign gifts to the Department of Education pursuant to the Higher Education Act, no such requirement exists for think tanks and other tax-exempt organizations.\n**(2)**\nThe Department of Defense found in its Military and Strategic Developments Involving the People\u2019s Republic of China 2019 Report that: China conducts influence operations against cultural institutions, media organizations, and the business, academic, and policy communities of the United States, other countries, and international institutions to achieve outcomes favorable to its security and military strategy objectives. \u2026 China harnesses academia and educational institutions, think tanks, and state-run media to advance its soft power campaign in support of China\u2019s security interests. .\n**(3)**\nAccording to the unclassified March 2025 Annual Threat Assessment of the United States Intelligence Community delivered to Congress, the Chinese government is likely to feel emboldened to use malign influence more regularly in coming years. The lack of transparency surrounding Chinese funding flows to organizations in the United States is a growing national security risk.\n**(4)**\nThe Chinese Communist Party (CCP) specifically targets think tanks as part of its united front work, which is a blend of engagement, influence activities, and intelligence operations used in part to shape policy toward China and gain access to technology. The Central United Front Work Department (UFWD), which reports directly to the CCP\u2019s Central Committee, is the lead organization for coordinating and carrying out united front work and oversees organizations operating in the United States, including in Washington, DC.\n**(5)**\nAccording to a Hoover Institution report, China\u2019s influence activities have moved beyond a traditional focus on diaspora communities to target a far broader range of sectors in Western societies, including think tanks, seeking to promote views sympathetic to the Chinese government and co-opt United States citizens to support China\u2019s foreign policy goals and economic interests.\n**(6)**\nSeveral think tanks, cultural organizations, and related entities incorporated in the United States have received money or other forms of support from the UFWD and its proxies and agents. A 2018 report by the U.S.-China Economic and Security Review Commission noted that a number of Washington, DC think tanks and universities have received funding from Tung Cheehwa, the head of a united front-affiliated organization called the China-United States Exchange Foundation (CUSEF).\n**(7)**\nIn May 2024, Bloomberg News reported that Optica Foundation, a United States-based 501(c)(3) tax exempt organization, secretly accepted millions of dollars from Huawei, which has been designated by the U.S. government as a national security threat, as part of a program to fund cutting-edge research.\n**(8)**\nAccording to a December 2023 letter led by the Chairman of the House Select Committee on the Strategic Competition Between the United States and the Chinese Communist Party, the Max Baucus Institute, a 501(c)(3) organization, was promoting a study trip for students to China that was funded by united front-affiliated CUSEF.\n**(9)**\nAccording to a November 2023 report by the House Select Committee on the Strategic Competition Between the United States and the Chinese Communist Party, China\u2019s intelligence agencies seek to draw on members of united front organizations to support espionage and influence operations, as seen in the law enforcement arrests relating to the CCP\u2019s police station in New York City. In April 2023, the CCP mobilized groups based in the United States with ties to its united front organizations to join protests against Taiwan\u2019s then-president who was transiting the United States.\n#### 3. Annual disclosure of contributions from foreign governments, foreign political parties, and other entities by certain tax-exempt organizations\n##### (a) Reporting requirement\nSection 6033(b) of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (15), by redesignating paragraph (16) as paragraph (17) and by inserting after paragraph (15) the following new paragraph:\n(16) with respect to each government of a foreign country (within the meaning of section 1(e) of the Foreign Agents Registration Act of 1938 ( 22 U.S.C. 611(e) )), each foreign political party (within the meaning of section 1(f) of such Act ( 22 U.S.C. 611(f) )), and each entity that is directed, controlled, financed, or subsidized (in whole or in part) by a foreign country specified in section 4872(f)(2) of title 10, or agent thereof, which made aggregate contributions and gifts to the organization during the year in excess of $10,000, the name of such government, political party, or entity and such aggregate amount, and .\n##### (b) Public disclosure\nSection 6104 of such Code is amended by adding at the end the following new subsection:\n(e) Public disclosure of certain information The Secretary shall make publicly available in a searchable database the following information: (1) The information furnished under section 6033(b)(16) of the Internal Revenue Code of 1986, as amended by this section. (2) The name of the organization furnishing the information described in paragraph (1). (3) The aggregate amount reported under such section as having been received as contributions or gifts in each year from\u2014 (A) the People\u2019s Republic of China, (B) the Chinese Communist Party, or (C) any entity directed, controlled, financed, or subsidized (in whole or in part) by an entity described in subparagraph (A) or (B) (or an agent thereof). .\n##### (c) Effective date\nThe amendments made by this section shall apply to returns filed for taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-06-12",
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
        "name": "Taxation",
        "updateDate": "2025-06-30T18:05:45Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3966ih.xml"
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
      "title": "Think Tank and Nonprofit Foreign Influence Disclosure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Think Tank and Nonprofit Foreign Influence Disclosure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for the public reporting of certain contributions received by charitable organizations from foreign governments and foreign political parties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T04:18:41Z"
    }
  ]
}
```
