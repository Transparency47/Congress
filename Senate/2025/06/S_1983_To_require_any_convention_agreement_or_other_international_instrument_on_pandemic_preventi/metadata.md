# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1983?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1983
- Title: No WHO Pandemic Preparedness Treaty Without Senate Approval Act
- Congress: 119
- Bill type: S
- Bill number: 1983
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2026-05-12T11:03:31Z
- Update date including text: 2026-05-12T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1983",
    "number": "1983",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000293",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Johnson, Ron [R-WI]",
        "lastName": "Johnson",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "No WHO Pandemic Preparedness Treaty Without Senate Approval Act",
    "type": "S",
    "updateDate": "2026-05-12T11:03:31Z",
    "updateDateIncludingText": "2026-05-12T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-06-05",
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
        "item": [
          {
            "date": "2025-06-05T18:55:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-06-05T18:55:12Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "WY"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "ND"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "ID"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "IA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "TN"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "ND"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "OK"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "UT"
    },
    {
      "bioguideId": "P000603",
      "firstName": "Rand",
      "fullName": "Sen. Paul, Rand [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "Paul",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "KY"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "ID"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "NC"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "AL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "WY"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MS"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "IA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1983is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1983\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Johnson (for himself, Mr. Barrasso , Mr. Budd , Mr. Cramer , Mr. Crapo , Mr. Grassley , Mr. Hagerty , Mr. Hoeven , Mr. Lankford , Mr. Lee , Mr. Paul , Mr. Risch , Mr. Scott of Florida , Mr. Tillis , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require any convention, agreement, or other international instrument on pandemic prevention, preparedness, and response reached by the World Health Assembly to be subject to Senate ratification.\n#### 1. Short title\nThis Act may be cited as the No WHO Pandemic Preparedness Treaty Without Senate Approval Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nOn May 18, 2020, President Donald Trump sent a letter to World Health Organization (referred to in this Act as WHO ) Director-General Tedros Adhanom Ghebreyesus (referred to in this Act as the Director-General ), announcing that\u2014\n**(A)**\nUnited States contributions to WHO would be halted due its mismanagement of the COVID\u201319 outbreak and its lack of independence from the People\u2019s Republic of China; and\n**(B)**\nthe United States would withdraw from WHO if it did not commit to substantive improvements within 30 days.\n**(2)**\nPresident Trump\u2019s May 18 letter cited numerous instances of WHO mismanagement of the COVID\u201319 pandemic, including\u2014\n**(A)**\nunjustified delays informing member states about a potentially serious disease outbreak in Wuhan, China; and\n**(B)**\nrepeated grossly inaccurate or misleading claims about the transmissibility of the virus and about the Government of China\u2019s handling of the outbreak.\n**(3)**\nOn June 30, 2020, Secretary of State Mike Pompeo formally notified the United Nations of the United States decision to withdraw from WHO, which would have taken effect on July 6, 2021, under the terms of a joint resolution adopted by Congress on June 14, 1948 ( Public Law 80\u2013643 ; 62 Stat. 441).\n**(4)**\nA Pew Research Center survey conducted in April and May 2020 indicated that 51 percent of Americans felt that WHO had done a poor or fair job in managing the COVID\u201319 pandemic.\n**(5)**\nOn January 20, 2021, President Joseph Biden sent United Nations Director-General Ant\u00f3nio Guterres a letter retracting the United States notice of withdrawal from WHO.\n**(6)**\nOn December 1, 2021, at the second special session of the World Health Assembly (referred to in this Act as the WHA ) decided\u2014\n**(A)**\nto establish an intergovernmental negotiating body (referred to in this section as the INB ) to draft and negotiate a WHO convention (referred to in this section as the Convention ), agreement, or other international instrument on pandemic prevention, preparedness, and response, with a view to adoption under Article 19 or any other provision of the WHO Constitution; and\n**(B)**\nthat the INB shall submit a progress report to the Seventy-sixth WHA and a working draft of the convention for consideration by the Seventy-seventh WHA.\n**(7)**\nOn February 24, March 14 and 15, and June 6 through 8 and 15 through 17, 2022, the INB held its inaugural meeting at which the Director-General proposed the following 5 themes to guide the INB\u2019s work in drafting the Convention:\n**(A)**\nBuilding national, regional, and global capacities based on a whole-of-government and whole-of-society approach.\n**(B)**\nEstablishing global access and benefit sharing for all pathogens, and determining a global policy for the equitable production and distribution of countermeasures.\n**(C)**\nEstablishing robust systems and tools for pandemic preparedness and response.\n**(D)**\nEstablishing a long-term plan for sustainable financing to ensure support for global health threat management and response systems.\n**(E)**\nEmpowering WHO to fulfill its mandate as the directing and coordinating authority on international health work, including for pandemic preparedness and response.\n**(8)**\nThe INB failed to negotiate an agreement on Convention text and did not present a final draft of the Convention during the Seventy-seventh World Health Assembly held between May 27 and June 1, 2024.\n**(9)**\nOn June 1, 2024, the World Health Assembly extended the INB\u2019s Convention mandate until the Seventy-eighth World Health Assembly in 2025.\n**(10)**\nOn January 20, 2025, President Donald Trump revoked President Joseph Biden\u2019s January 25, 2021, retraction of the United States notification of withdrawal from the WHO.\n**(11)**\nOn May 20, 2025, during the 78th World Health Assembly, WHO member states adopted the INB\u2019s draft of a WHO Pandemic Agreement.\n**(12)**\nSection 723.3 of title 11 of the Department of State\u2019s Foreign Affairs Manual states that when determining whether any international agreement should be brought into force as a treaty or as an international agreement other than a treaty, the utmost care is to be exercised to avoid any invasion or compromise of the constitutional powers of the President, the Senate, and the Congress as a whole and includes the following criteria to be considered when determining whether an international agreement should take the form of a treaty or an executive agreement:\n**(A)**\nThe extent to which the agreement involves commitments or risks affecting the nation as a whole .\n**(B)**\nWhether the agreement is intended to affect state laws .\n**(C)**\nWhether the agreement can be given effect without the enactment of subsequent legislation by the Congress .\n**(D)**\nPast U.S. practice as to similar agreements .\n**(E)**\nThe preference of the Congress as to a particular type of agreement .\n**(F)**\nThe degree of formality desired for an agreement .\n**(G)**\nThe proposed duration of the agreement, the need for prompt conclusion of an agreement, and the desirability of concluding a routine or short-term agreement .\n**(H)**\nThe general international practice as to similar agreements .\n#### 3. Sense of the Senate\nIt is the sense of the Senate that\u2014\n**(1)**\na significant segment of the American public is deeply skeptical of the World Health Organization, its leadership, and its independence from the pernicious political influence of certain member states, including the People's Republic of China;\n**(2)**\nthe Senate strongly prefers that any agreement related to pandemic prevention, preparedness, and response adopted by the World Health Assembly pursuant to the work of the INB be considered a treaty requiring the advice and consent of the Senate, with two-thirds of Senators concurring;\n**(3)**\nthe scope of the agreement which the INB has been tasked with drafting, as outlined by the Director-General, is so broad that any application of the factors referred to in section 2(11) will weigh strongly in favor of it being considered a treaty; and\n**(4)**\ngiven the level of public distrust, any relevant new agreement by the World Health Assembly which cannot garner the two-thirds vote needed for Senate approval should not be agreed to or implemented by the United States.\n#### 4. Any World Health Assembly convention or agreement or other international instrument resulting from the International Negotiating Body\u2019s final report deemed to be a treaty subject to advice and consent of the Senate\nNotwithstanding any other provision of law, any convention, agreement, or other international instrument on pandemic prevention, preparedness, and response reached by the World Health Assembly pursuant to the recommendations, report, or work of the International Negotiating Body established by the second special session of the World Health Assembly is deemed to be a treaty that is subject to the requirements of article II, section 2, clause 2 of the Constitution of the United States, which requires the advice and consent of the Senate, with two-thirds of Senators concurring.",
      "versionDate": "2025-06-05",
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
        "actionDate": "2025-06-26",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "4207",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No WHO Pandemic Preparedness Treaty Without Senate Approval Act",
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
        "name": "International Affairs",
        "updateDate": "2025-07-17T20:04:45Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1983is.xml"
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
      "title": "No WHO Pandemic Preparedness Treaty Without Senate Approval Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No WHO Pandemic Preparedness Treaty Without Senate Approval Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require any convention, agreement, or other international instrument on pandemic prevention, preparedness, and response reached by the World Health Assembly to be subject to Senate ratification.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:23Z"
    }
  ]
}
```
