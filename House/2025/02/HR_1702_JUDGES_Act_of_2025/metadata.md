# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1702?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1702
- Title: JUDGES Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1702
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-28T08:05:52Z
- Update date including text: 2026-04-28T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-05 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 11.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-05 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-05 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 11.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1702",
    "number": "1702",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "I000056",
        "district": "48",
        "firstName": "Darrell",
        "fullName": "Rep. Issa, Darrell [R-CA-48]",
        "lastName": "Issa",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "JUDGES Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:52Z",
    "updateDateIncludingText": "2026-04-28T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 11.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
        "item": [
          {
            "date": "2025-03-05T20:17:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-27T14:13:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "OK"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MO"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IN"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "ID"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "CA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "NE"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "CA"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "CO"
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
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1702ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1702\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Issa (for himself, Ms. Lee of Florida , Mr. Nehls , and Mr. Kiley of California ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize additional district judges for the district courts and convert temporary judgeships.\n#### 1. Short title\nThis Act may be cited as the Judicial Understaffing Delays Getting Emergencies Solved Act of 2025 or the JUDGES Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArticle III of the Constitution of the United States gives Congress the power to establish judgeships in the district courts of the United States.\n**(2)**\nCongress has not created a new district court judgeship since 2003 and has not enacted comprehensive judgeship legislation since 1990.\n**(3)**\nThis represents the longest period of time since district courts of the United States were established in 1789 that Congress has not authorized any new permanent district court judgeships.\n**(4)**\nBy the end of fiscal year 2022, filings in the district courts of the United States had increased by 30 percent since the last comprehensive judgeship legislation.\n**(5)**\nAs of March 31, 2023, there were 686,797 pending cases in the district courts of the United States, with an average of 491 weighted case filings per judgeship over a 12-month period.\n**(6)**\nTo deal with increased filings in the district courts of the United States, the Judicial Conference of the United States requested the creation of 66 new district court judgeships in its 2023 report.\n#### 3. Additional district judges for the district courts\n##### (a) Additional judgeships\n**(1) 2025**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the central district of California;\n**(ii)**\n1 additional district judge for the eastern district of California;\n**(iii)**\n1 additional district judge for the northern district of California;\n**(iv)**\n1 additional district judge for the district of Delaware;\n**(v)**\n1 additional district judge for the middle district of Florida;\n**(vi)**\n1 additional district judge for the southern district of Indiana;\n**(vii)**\n1 additional district judge for the northern district of Iowa;\n**(viii)**\n1 additional district judge for the district of New Jersey;\n**(ix)**\n1 additional district judge for the southern district of New York;\n**(x)**\n1 additional district judge for the eastern district of Texas; and\n**(xi)**\n1 additional district judge for the southern district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 15 Eastern 7 Central 28 Southern 13 ;\n**(ii)**\nby striking the item relating to Delaware and inserting the following:\nDelaware 5 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 16 Southern 17 ;\n**(iv)**\nby striking the items relating to Indiana and inserting the following:\nIndiana: Northern 5 Southern 6 ;\n**(v)**\nby striking the items relating to Iowa and inserting the following:\nIowa: Northern 3 Southern 3 ;\n**(vi)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 18 ;\n**(vii)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 15 Western 4 ; and\n**(viii)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 12 Southern 20 Eastern 8 Western 13 .\n**(C) Effective date**\nThis paragraph shall take effect on the date of the enactment of this Act.\n**(2) 2027**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the district of Arizona;\n**(ii)**\n2 additional district judges for the central district of California;\n**(iii)**\n1 additional district judge for the eastern district of California;\n**(iv)**\n1 additional district judge for the northern district of California;\n**(v)**\n1 additional district judge for the middle district of Florida;\n**(vi)**\n1 additional district judge for the southern district of Florida;\n**(vii)**\n1 additional district judge for the northern district of Georgia;\n**(viii)**\n1 additional district judge for the district of Idaho;\n**(ix)**\n1 additional district judge for the northern district of Texas; and\n**(x)**\n1 additional district judge for the southern district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (1) of this subsection, is amended\u2014\n**(i)**\nby striking the item relating to Arizona and inserting the following:\nArizona 13 ;\n**(ii)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 16 Eastern 8 Central 30 Southern 13 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 17 Southern 18 ;\n**(iv)**\nby striking the items relating to Georgia and inserting the following:\nGeorgia: Northern 12 Middle 4 Southern 3 ;\n**(v)**\nby striking the item relating to Idaho and inserting the following:\nIdaho 3 ; and\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 21 Eastern 8 Western 13 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2027.\n**(3) 2029**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the central district of California;\n**(ii)**\n1 additional district judge for the eastern district of California;\n**(iii)**\n1 additional district judge for the northern district of California;\n**(iv)**\n1 additional district judge for the district of Colorado;\n**(v)**\n1 additional district judge for the district of Delaware;\n**(vi)**\n1 additional district judge for the district of Nebraska;\n**(vii)**\n1 additional district judge for the eastern district of New York;\n**(viii)**\n1 additional district judge for the northern district of Oklahoma;\n**(ix)**\n1 additional district judge for the eastern district of Texas;\n**(x)**\n1 additional district judge for the southern district of Texas; and\n**(xi)**\n1 additional district judge for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (2) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 17 Eastern 9 Central 31 Southern 13 ;\n**(ii)**\nby striking the item relating to Colorado and inserting the following:\nColorado 8 ;\n**(iii)**\nby striking the item relating to Delaware and inserting the following:\nDelaware 6 ;\n**(iv)**\nby striking the item relating to Nebraska and inserting the following:\nNebraska 4 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 16 Western 4 ;\n**(vi)**\nby striking the items relating to Oklahoma and inserting the following:\nOklahoma: Northern 4 Eastern 1 Western 6 Northern, Eastern,and Western 1 ; and\n**(vii)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 22 Eastern 9 Western 14 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2029.\n**(4) 2031**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n1 additional district judge for the district of Arizona;\n**(ii)**\n1 additional district judge for the central district of California;\n**(iii)**\n1 additional district judge for the eastern district of California;\n**(iv)**\n1 additional district judge for the northern district of California;\n**(v)**\n1 additional district judge for the southern district of California;\n**(vi)**\n1 additional district judge for the middle district of Florida;\n**(vii)**\n1 additional district judge for the southern district of Florida;\n**(viii)**\n1 additional district judge for the district of New Jersey;\n**(ix)**\n1 additional district judge for the western district of New York; and\n**(x)**\n2 additional district judges for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (3) of this subsection, is amended\u2014\n**(i)**\nby striking the item relating to Arizona and inserting the following:\nArizona 14 ;\n**(ii)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 18 Eastern 10 Central 32 Southern 14 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 4 Middle 18 Southern 19 ;\n**(iv)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 19 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 29 Eastern 16 Western 5 ; and\n**(vi)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 22 Eastern 9 Western 16 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2031.\n**(5) 2033**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n2 additional district judges for the central district of California;\n**(ii)**\n1 additional district judge for the northern district of California;\n**(iii)**\n1 additional district judge for the district of Colorado;\n**(iv)**\n1 additional district judge for the middle district of Florida;\n**(v)**\n1 additional district judge for the northern district of Florida;\n**(vi)**\n1 additional district judge for the northern district of Georgia;\n**(vii)**\n1 additional district judge for the southern district of New York;\n**(viii)**\n1 additional district judge for the eastern district of Oklahoma;\n**(ix)**\n1 additional district judge for the southern district of Texas; and\n**(x)**\n1 additional district judge for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (4) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 19 Eastern 10 Central 34 Southern 14 ;\n**(ii)**\nby striking the item relating to Colorado and inserting the following:\nColorado 9 ;\n**(iii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 5 Middle 19 Southern 19 ;\n**(iv)**\nby striking the items relating to Georgia and inserting the following:\nGeorgia: Northern 13 Middle 4 Southern 3 ;\n**(v)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 30 Eastern 16 Western 5 ;\n**(vi)**\nby striking the items relating to Oklahoma and inserting the following:\nOklahoma: Northern 4 Eastern 2 Western 6 Northern, Eastern,and Western 1 ; and\n**(vii)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 23 Eastern 9 Western 17 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2033.\n**(6) 2035**\n**(A) In general**\nThe President shall appoint, by and with the advice and consent of the Senate\u2014\n**(i)**\n2 additional district judges for the central district of California;\n**(ii)**\n1 additional district judge for the northern district of California;\n**(iii)**\n1 additional district judge for the southern district of California;\n**(iv)**\n1 additional district judge for the middle district of Florida;\n**(v)**\n1 additional district judge for the southern district of Florida;\n**(vi)**\n1 additional district judge for the district of New Jersey;\n**(vii)**\n1 additional district judge for the eastern district of New York; and\n**(viii)**\n2 additional district judges for the western district of Texas.\n**(B) Tables**\nThe table contained in section 133(a) of title 28, United States Code, as amended by paragraph (5) of this subsection, is amended\u2014\n**(i)**\nby striking the items relating to California and inserting the following:\nCalifornia: Northern 20 Eastern 10 Central 36 Southern 15 ;\n**(ii)**\nby striking the items relating to Florida and inserting the following:\nFlorida: Northern 5 Middle 20 Southern 20 ;\n**(iii)**\nby striking the item relating to New Jersey and inserting the following:\nNew Jersey 20 ;\n**(iv)**\nby striking the items relating to New York and inserting the following:\nNew York: Northern 5 Southern 30 Eastern 17 Western 5 ; and\n**(v)**\nby striking the items relating to Texas and inserting the following:\nTexas: Northern 13 Southern 23 Eastern 9 Western 19 .\n**(C) Effective date**\nThis paragraph shall take effect on January 21, 2035.\n##### (b) Temporary judgeships\n**(1) In general**\nThe President shall appoint, by and with the advice and consent of the Senate, 1 additional district judge for the eastern district of Oklahoma.\n**(2) Vacancies not filled**\nThe first vacancy in the office of district judge in each of the offices of district judge authorized by this subsection, occurring 5 years or more after the confirmation date of the judge named to fill the temporary district judgeship created in the applicable district by this subsection, shall not be filled.\n**(3) Effective date**\nThis subsection shall take effect on the date of the enactment of this Act.\n##### (c) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section and the amendments made by this section\u2014\n**(A)**\nfor each of fiscal years 2025 and 2026, $12,965,330;\n**(B)**\nfor each of fiscal years 2027 and 2028, $23,152,375;\n**(C)**\nfor each of fiscal years 2029 and 2030, $32,413,325;\n**(D)**\nfor each of fiscal years 2031 and 2032, $42,600,370;\n**(E)**\nfor each of fiscal years 2033 and 2034, $51,861,320; and\n**(F)**\nfor fiscal year 2035 and each fiscal year thereafter, $61,122,270.\n**(2) Inflation adjustment**\nFor each fiscal year described in paragraph (1), the amount authorized to be appropriated for such fiscal year shall be increased by the percentage by which\u2014\n**(A)**\nthe Consumer Price Index for the previous fiscal year, exceeds\n**(B)**\nthe Consumer Price Index for the fiscal year preceding the fiscal year described in subparagraph (A).\n**(3) Definition**\nIn this subsection, the term Consumer Price Index means the Consumer Price Index for All Urban Consumers (all items, United States city average), published by the Bureau of Labor Statistics of the Department of Labor.\n#### 4. Organization of Texas district courts\nSection 124(b)(2) of title 28, United States Code, is amended, in the matter preceding paragraph (3), by inserting and College Station before the period at the end.\n#### 5. Organization of California district courts\nSection 84(d) of title 28, United States Code, is amended by inserting and El Centro after at San Diego .\n#### 6. GAO reports\n##### (a) Judicial caseloads\nNot later than 2 years after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives and make publicly available reports\u2014\n**(1)**\nevaluating\u2014\n**(A)**\nthe accuracy and objectiveness of case-related workload measures and methodologies used by the Administrative Office of the United States Courts for district courts of the United States and courts of appeals of the United States;\n**(B)**\nthe impact of non-case-related activities of judges of the district courts of the United States and courts of appeals of the United States on judicial caseloads; and\n**(C)**\nthe effectiveness and efficiency of the policies of the Administrative Office of the United States Courts regarding senior judges; and\n**(2)**\nproviding any recommendations of the Comptroller General with respect to the matters described in paragraph (1).\n##### (b) Detention space\nThe Comptroller General of the United States shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on an assessment of\u2014\n**(1)**\na determination of the needs of Federal agencies for detention space;\n**(2)**\nefforts by Federal agencies to acquire detention space; and\n**(3)**\nany challenges in determining and acquiring detention space.\n#### 7. Public accessibility of the article III judgeship recommendations of the Judicial Conference of the United States report\n##### (a) In general\nThe Administrative Office of the United States Courts, in consultation with the Judicial Conference of the United States, shall make publicly available on their website, free of charge, the biennial report entitled Article III Judgeship Recommendations of the Judicial Conference of the United States .\n##### (b) Contents\nThe report described in subsection (a) should be released not less frequently than biennially and contain the summaries and all related appendixes supporting the judgeship recommendations of the Judicial Conference of the United States, including\u2014\n**(1)**\nthe process used by the Judicial Conference in developing the recommendations;\n**(2)**\nany caseload and methodology changes;\n**(3)**\njudgeship surveys with recommendations; and\n**(4)**\nspecific information about each court for which the Judicial Conference recommends additional judgeships.\n##### (c) Submission to Congress\nThe Administrative Office of the United States Courts shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives copies of the report described in subsection (a).",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-13",
        "actionTime": "10:56:41",
        "text": "Held at the desk."
      },
      "number": "32",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LACA",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "625",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LACA",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1929",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "JUDGES Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Arizona",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "California",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Colorado",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Delaware",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Florida",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Georgia",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Idaho",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Indiana",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Iowa",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Judges",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Nebraska",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "New Jersey",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "New York State",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Oklahoma",
            "updateDate": "2025-03-18T14:24:55Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-03-18T14:24:54Z"
          },
          {
            "name": "Utah",
            "updateDate": "2025-03-18T14:24:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-03-14T11:53:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1702",
          "measure-number": "1702",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1702v00",
            "update-date": "2026-02-12"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Judicial Understaffing Delays Getting Emergencies Solved Act of 2025 or the JUDGES Act of 2025</strong></p><p>This bill creates 64 U.S. district court judgeships\u201463 permanent and 1 temporary\u2014and expands the jurisdictional coverage of two district courts.</p><p>Specifically, the bill creates 63 new permanent judgeships across 14 states over a 10-year period beginning in 2025. The state and total number of judgeships added over the 10-year period are as follows:</p><ul><li>Arizona (1),\u00a0</li><li>California (20),</li><li>Colorado (2),</li><li>Delaware (2),</li><li>Florida (9),</li><li>Georgia (2),</li><li>Idaho (1),</li><li>Indiana (1),</li><li>Iowa (1),</li><li>Nebraska (1),</li><li>New Jersey (3),</li><li>New York (5),</li><li>Oklahoma (2), and</li><li>Texas (13).</li></ul><p>Additionally, the bill creates one temporary judgeship in the Eastern District of Oklahoma in 2025.</p><p>Finally, the bill adds locations where court must be held in two district courts\u2014one in California and one in Texas. Specifically, the bill adds College Station to the list of places where court must be held in the Houston Division of the Southern District of Texas. Also, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p><p>The bill directs the Government Accountability Office to submit reports to Congress on judicial caseloads and detention space.</p><p>The bill also directs the Administrative Office of the U.S. Courts to make available on its website the biennial report by the Judicial Conference of the United States on judgeship recommendations. \u00a0</p>"
        },
        "title": "JUDGES Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1702.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Judicial Understaffing Delays Getting Emergencies Solved Act of 2025 or the JUDGES Act of 2025</strong></p><p>This bill creates 64 U.S. district court judgeships\u201463 permanent and 1 temporary\u2014and expands the jurisdictional coverage of two district courts.</p><p>Specifically, the bill creates 63 new permanent judgeships across 14 states over a 10-year period beginning in 2025. The state and total number of judgeships added over the 10-year period are as follows:</p><ul><li>Arizona (1),\u00a0</li><li>California (20),</li><li>Colorado (2),</li><li>Delaware (2),</li><li>Florida (9),</li><li>Georgia (2),</li><li>Idaho (1),</li><li>Indiana (1),</li><li>Iowa (1),</li><li>Nebraska (1),</li><li>New Jersey (3),</li><li>New York (5),</li><li>Oklahoma (2), and</li><li>Texas (13).</li></ul><p>Additionally, the bill creates one temporary judgeship in the Eastern District of Oklahoma in 2025.</p><p>Finally, the bill adds locations where court must be held in two district courts\u2014one in California and one in Texas. Specifically, the bill adds College Station to the list of places where court must be held in the Houston Division of the Southern District of Texas. Also, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p><p>The bill directs the Government Accountability Office to submit reports to Congress on judicial caseloads and detention space.</p><p>The bill also directs the Administrative Office of the U.S. Courts to make available on its website the biennial report by the Judicial Conference of the United States on judgeship recommendations. \u00a0</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr1702"
    },
    "title": "JUDGES Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Judicial Understaffing Delays Getting Emergencies Solved Act of 2025 or the JUDGES Act of 2025</strong></p><p>This bill creates 64 U.S. district court judgeships\u201463 permanent and 1 temporary\u2014and expands the jurisdictional coverage of two district courts.</p><p>Specifically, the bill creates 63 new permanent judgeships across 14 states over a 10-year period beginning in 2025. The state and total number of judgeships added over the 10-year period are as follows:</p><ul><li>Arizona (1),\u00a0</li><li>California (20),</li><li>Colorado (2),</li><li>Delaware (2),</li><li>Florida (9),</li><li>Georgia (2),</li><li>Idaho (1),</li><li>Indiana (1),</li><li>Iowa (1),</li><li>Nebraska (1),</li><li>New Jersey (3),</li><li>New York (5),</li><li>Oklahoma (2), and</li><li>Texas (13).</li></ul><p>Additionally, the bill creates one temporary judgeship in the Eastern District of Oklahoma in 2025.</p><p>Finally, the bill adds locations where court must be held in two district courts\u2014one in California and one in Texas. Specifically, the bill adds College Station to the list of places where court must be held in the Houston Division of the Southern District of Texas. Also, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p><p>The bill directs the Government Accountability Office to submit reports to Congress on judicial caseloads and detention space.</p><p>The bill also directs the Administrative Office of the U.S. Courts to make available on its website the biennial report by the Judicial Conference of the United States on judgeship recommendations. \u00a0</p>",
      "updateDate": "2026-02-12",
      "versionCode": "id119hr1702"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1702ih.xml"
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
      "title": "JUDGES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "JUDGES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Judicial Understaffing Delays Getting Emergencies Solved Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize additional district judges for the district courts and convert temporary judgeships.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:36Z"
    }
  ]
}
```
