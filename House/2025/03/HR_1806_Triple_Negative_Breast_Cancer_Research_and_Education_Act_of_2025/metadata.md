# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1806?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1806
- Title: Triple-Negative Breast Cancer Research and Education Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1806
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2026-05-23T08:07:22Z
- Update date including text: 2026-05-23T08:07:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1806",
    "number": "1806",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001206",
        "district": "25",
        "firstName": "Joseph",
        "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
        "lastName": "Morelle",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Triple-Negative Breast Cancer Research and Education Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:22Z",
    "updateDateIncludingText": "2026-05-23T08:07:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NE"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "FL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "DC"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "PA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NJ"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "MI"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MD"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-05-22",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1806ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1806\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Mr. Morelle (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for research and education with respect to triple-negative breast cancer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Triple-Negative Breast Cancer Research and Education Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nBreast cancer accounts for 1 in 4 cancer diagnoses among women in this country.\n**(2)**\nThe survival rate for breast cancer has increased to 90 percent for White women and 78 percent for African-American women.\n**(3)**\nAfrican-American women are more likely to be diagnosed with larger tumors and more advanced stages of breast cancer despite a lower incidence rate.\n**(4)**\nEarly detection for breast cancer increases survival rates for breast cancer, as evidenced by a 5-year relative survival rate of 98 percent for breast cancers that are discovered before the cancer spreads beyond the breast, compared to 23 percent for stage IV breast cancers.\n**(5)**\nTriple-negative breast cancer is a term used to describe breast cancers whose cells do not have estrogen receptors and progesterone receptors, and do not have an excess of the HER2 protein on their sources.\n**(6)**\nIt is estimated that between 10 and 20 percent of female breast cancer patients are diagnosed with triple-negative breast cancer, and studies indicate the prevalence of triple-negative breast cancer is much higher.\n**(7)**\nTriple-negative breast cancer most commonly affects African-American women, followed by Hispanic women.\n**(8)**\nTriple-negative breast cancer is a very aggressive form of cancer which affects women under the age of 50 across all racial and socioeconomic backgrounds.\n**(9)**\nAfrican-American women are 3 times more likely to develop triple-negative breast cancer than White women.\n**(10)**\nTriple-negative breast cancer tends to grow and spread more quickly than most other types of breast cancer.\n**(11)**\nLike other forms of breast cancer, triple-negative breast cancer is treated with surgery, radiation therapy, or chemotherapy.\n**(12)**\nEarly-stage detection of triple-negative breast cancer is the key to survival because the tumor cells lack certain receptors, and neither hormone therapy nor drugs that target these receptors are effective against these cancers; therefore, early detection and education is vital.\n**(13)**\nCurrent research and available data do not provide adequate information on\u2014\n**(A)**\nthe rates of prevalence and incidence of triple-negative breast cancer in African-American, Hispanic, and other minority women;\n**(B)**\nthe costs associated with treating triple-negative breast cancer; and\n**(C)**\nthe methods by which triple-negative breast cancer may be prevented or cured in these women.\n#### 3. Triple-negative breast cancer\nSubpart I of part C of title IV of the Public Health Service Act ( 42 U.S.C. 285 et seq. ) is amended by inserting after section 417A ( 42 U.S.C. 285a\u20137 ) the following:\n417B. Triple-negative breast cancer (a) Research (1) In general The Director of the National Institutes of Health (in this section referred to as the Director of NIH ) shall expand, intensify, and coordinate programs for the conduct and support of research with respect to triple-negative breast cancer. (2) Administration The Director of NIH shall carry out this subsection through the appropriate institutes, offices, and centers of the National Institutes of Health, including the Eunice Kennedy Shriver National Institute of Child Health and Human Development, the National Institute of Environmental Health Sciences, the Office of Research on Women\u2019s Health, and the National Institute on Minority Health and Health Disparities. (3) Coordination of activities The Director of the Office of Research on Women\u2019s Health shall coordinate activities under this subsection among the institutes, offices, and centers of the National Institutes of Health. (4) Authorization of appropriations For the purposes of carrying out this subsection, there are authorized to be appropriated such sums as may be necessary for each of the fiscal years 2026 through 2031. (b) Education and dissemination of information with respect to triple-Negative breast cancer (1) Triple-Negative breast cancer public education program The Secretary of Health and Human Services, acting through the Director of the Centers for Disease Control and Prevention, shall develop and disseminate to the public information regarding triple-negative breast cancer, including information on\u2014 (A) the incidence and prevalence of triple-negative breast cancer among women; (B) the elevated risk for minority women to develop triple-negative breast cancer; and (C) the availability, as medically appropriate, of a range of treatment options for symptomatic triple-negative breast cancer. (2) Dissemination of information The Secretary may disseminate information under paragraph (1) directly or through arrangements with nonprofit organizations, consumer groups, institutions of higher education, Federal, State, or local agencies, or the media. (3) Authorization of appropriations For the purpose of carrying out this subsection, there are authorized to be appropriated such sums as may be necessary for each of the fiscal years 2026 through 2031. (c) Information to health care providers with respect to triple-Negative breast cancer (1) Dissemination of information The Secretary of Health and Human Services, acting through the Administrator of the Health Resources and Services Administration, shall develop and disseminate to health care providers information on triple-negative breast cancer for the purpose of ensuring that health care providers remain informed about current information on triple-negative breast cancer. Such information shall include the elevated risk for minority women to develop triple-negative breast cancer and the range of available options for the treatment of symptomatic triple-negative breast cancer. (2) Authorization of appropriations For the purpose of carrying out this subsection, there are authorized to be appropriated such sums as may be necessary for each of the fiscal years 2026 through 2031. (d) Definition In this section, the term minority women means women who are members of a racial and ethnic minority group, as defined in section 1707(g). .",
      "versionDate": "2025-03-03",
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
        "name": "Health",
        "updateDate": "2025-03-21T15:43:16Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1806ih.xml"
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
      "title": "Triple-Negative Breast Cancer Research and Education Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Triple-Negative Breast Cancer Research and Education Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for research and education with respect to triple-negative breast cancer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:34Z"
    }
  ]
}
```
