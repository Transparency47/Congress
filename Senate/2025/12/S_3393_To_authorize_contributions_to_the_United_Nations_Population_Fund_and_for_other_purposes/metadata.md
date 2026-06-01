# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3393?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3393
- Title: Support UNFPA Funding Act
- Congress: 119
- Bill type: S
- Bill number: 3393
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-01-06T19:58:50Z
- Update date including text: 2026-01-06T19:58:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3393",
    "number": "3393",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Support UNFPA Funding Act",
    "type": "S",
    "updateDate": "2026-01-06T19:58:50Z",
    "updateDateIncludingText": "2026-01-06T19:58:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-09",
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
          "date": "2025-12-09T19:28:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "DE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CO"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-09",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VT"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3393is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3393\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mrs. Shaheen (for herself, Mr. Durbin , Mrs. Murray , Mr. Coons , Mr. Kaine , Mr. Booker , Ms. Cortez Masto , Ms. Duckworth , Mrs. Gillibrand , Mr. Hickenlooper , Mr. Merkley , Ms. Rosen , Mr. Sanders , Mr. Schiff , Mr. Van Hollen , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo authorize contributions to the United Nations Population Fund, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support UNFPA Funding Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe United Nations Population Fund (referred to in this Act as UNFPA ) is the United Nations sexual and reproductive health agency.\n**(2)**\nUNFPA was founded with the bipartisan leadership of the United States and advances United States strategic interests to promote peace and stability overseas by working in more than 150 countries to end preventable maternal deaths, the unmet need for contraception, and gender-based violence and other harmful practices, including female genital mutilation and child marriage.\n**(3)**\nUNFPA is the United Nations agency with the mandate to provide reproductive and maternal care in humanitarian crises that are critical to the lives of women and girls by providing family planning, maternal health care, midwife training, and interventions to halt child marriage and the practice of female genital mutilation.\n**(4)**\nUNFPA is present in more than three times as many countries as United States bilateral family planning and reproductive health programs.\n**(5)**\nThe Multilateral Organization Performance Assessment Network (commonly known as MOPAN ), of which the United States is a member, conducted a thorough evaluation of UNFPA\u2019s organizational performance, effectiveness, and results. The evaluation, released in January 2025, concluded that UNFPA is an effective organization that is successfully delivering on its mandate. UNFPA has been an excellent steward and partner to the United States, ensuring that all United States financial contributions are kept in a segregated account and in compliance with United States legal restrictions. UNFPA does not fund abortion or promote abortion as a method of family planning. UNFPA opposes all forms of coercion and involuntary sterilization.\n**(6)**\nAll UNFPA programming is guided by principles adopted by 179 governments, including the United States, at the 1994 International Conference for Population and Development. The principles include that reproductive health care programs should provide the widest range of services without any form of coercion. All couples and individuals have the basic right to decide freely and responsibly the number and spacing of their children and to have the information, education and means to do so. .\n**(7)**\nUNFPA extends and supports the United States investment in global safety, stability and security by reaching women and girls in politically unstable regions. UNFPA also plays a pivotal role in meeting protection and health care needs in countries experiencing complex humanitarian emergencies.\n**(8)**\nUNFPA ensures access to health care and essential supplies for women and families affected by humanitarian crises, including those arising from natural disasters, armed conflicts, and other emergencies.\n**(9)**\nDuring 2024, UNFPA assisted millions of women, girls, and adolescents with a range of life-saving services, including\u2014\n**(A)**\n10,000,000 people who were reached with sexual and reproductive health services across 49 countries;\n**(B)**\n3,600,000 people who were reached with gender-based violence prevention, risk mitigation, and response services in 53 countries;\n**(C)**\nmore than 825,000 women who were assisted with delivering babies safely in 37 countries; and\n**(D)**\n3,500 health facilities that were supported in 55 countries, including conflict-affected countries where UNFPA is able to reach up to three times as many communities as United States services providers.\n**(10)**\nThe United States termination of funding for UNFPA programs restricts UNFPA\u2019s critical work, endangering lives across the world. Without such funding, UNFPA cannot continue to address the needs of\u2014\n**(A)**\nmore than 700 women and adolescent girls who die each day from preventable causes related to pregnancy and childbirth, most of which occur in developing countries and more than half of which occur in fragile and humanitarian settings;\n**(B)**\nmore than 226,000,000 women of reproductive age in low- and middle-income countries who want to avoid pregnancy and are not using a modern contraceptive method;\n**(C)**\nan estimated 1 in 3 women who experience gender-based violence;\n**(D)**\nan estimated 230,000,000 women who have survived some form of female genital mutilation; and\n**(E)**\nan estimated 12,000,000 girls who are forcibly married each year before reaching 18 years of age.\n**(11)**\nThe halting of United States funding in 2025 has already led to\u2014\n**(A)**\nthe closure of 21 health centers in Afghanistan, with 500 more health centers potentially facing closure;\n**(B)**\n200,000 women in Sudan who have been left without essential reproductive health services;\n**(C)**\nthe loss of lifesaving services for 1,500,000 women and girls in Yemen and the closing of 44 health facilities, 24 women-friendly spaces, and 14 mobile protection teams to reach the most vulnerable women in Yemen; and\n**(D)**\nthe discontinuation of hospital support in Bangladesh, including staff and medicines leading to limited life-saving emergency obstetric and newborn care impacting 11,000 women and girls in Bangladesh.\n**(12)**\nVoluntary family planning is central to global health, equality, and women\u2019s empowerment, and is a key factor in poverty reduction, enabling individuals and families to make informed decisions about their reproductive health and economic well-being.\n**(13)**\nProviding access to family planning\u2014\n**(A)**\nreduces unintended pregnancies and unsafe abortions; and\n**(B)**\nimproves the health outcomes of women.\n**(14)**\nGreater access to family planning has the potential\u2014\n**(A)**\nto prevent up to 30 percent of the 295,000 maternal deaths that occur annually; and\n**(B)**\nto save the lives of 1,400,000 children who are younger than 5 years of age.\n**(15)**\nIn March 2025, thousands of Americans, representing all 50 States, expressed their support for the lifesaving work of UNFPA through a series of letters.\n#### 3. Statement of policy\nIt is the policy of the United States that\u2014\n**(1)**\nimproving the health and status of women around the world is a strategic priority for United States foreign policy and development efforts that contributes to global stability and economic growth;\n**(2)**\nthe ability of individuals to freely determine whether, when, and with whom to have children, and to attain the highest standard of health, supports both human rights and sustainable development, fostering more stable and prosperous societies;\n**(3)**\nproviding access to voluntary contraception and reproductive health care is a cost-effective way to enhance women\u2019s economic participation, reduce poverty, and strengthen communities, advancing United States strategic interests;\n**(4)**\nUNFPA is a key partner in advancing global health, stability, and economic development by improving the health and status of women and expanding access to voluntary family planning and reproductive health care;\n**(5)**\nUNFPA plays a vital role in ensuring that family planning and reproductive health programs are voluntary, rights-based, and aligned with international standards, helping to prevent instability and improve health outcomes in vulnerable regions;\n**(6)**\nfinancial support for UNFPA aligns with United States interests by promoting global health, reducing maternal mortality, and fostering development in ways that contribute to more stable and self-sufficient nations; and\n**(7)**\nthe United States Government remains committed to providing targeted, cost-effective funding to support the efforts described in paragraphs (1) through (6).\n#### 4. Authorization of appropriations\n##### (a) Finding\nCongress finds that the United Nations Population Fund does not support nor participate in the management of any program or activity of coercive abortion or involuntary sterilization in any country.\n##### (b) Funding authority\nNotwithstanding any other provision of law, the United Nations Population Fund is authorized to receive funding, except with regards to programs in China.\n##### (c) Funding for fiscal years 2026 and 2027\n**(1) In general**\nThere is authorized to be appropriated to the President, in addition to funds otherwise made available, $74,000,000 for each of fiscal years 2026 and 2027 to support the core functions and programs of the United Nations Population Fund, which may include efforts\u2014\n**(A)**\nto end preventable maternal deaths;\n**(B)**\nto end the unmet need for contraceptives and promoting a voluntary approach to family planning;\n**(C)**\nto end gender-based violence;\n**(D)**\nto end other harmful practices, such as child marriage and female genital mutilation; and\n**(E)**\nin support of United States national security and humanitarian efforts by operating in areas where medical infrastructure or services have been destroyed or limited by natural disasters, armed conflict, or other humanitarian emergencies.\n**(2) Availability**\nAmounts appropriated pursuant to paragraph (1) shall remain available until expended.",
      "versionDate": "2025-12-09",
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
        "name": "International Affairs",
        "updateDate": "2026-01-06T19:58:50Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3393is.xml"
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
      "title": "Support UNFPA Funding Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Support UNFPA Funding Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to authorize contributions to the United Nations Population Fund, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:48:25Z"
    }
  ]
}
```
