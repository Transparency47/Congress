# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1725?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1725
- Title: Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1725
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-10-11T08:05:20Z
- Update date including text: 2025-10-11T08:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Economic Opportunity.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1725",
    "number": "1725",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-11T08:05:20Z",
    "updateDateIncludingText": "2025-10-11T08:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
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
        "item": {
          "date": "2025-02-27T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T17:58:43Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "SC"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MS"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "WA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "WI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-03",
      "state": "DC"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MI"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NV"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "IL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NY"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OH"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "CT"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1725ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1725\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Moulton (for himself and Mr. Clyburn ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to extend to Black veterans of World War II, and surviving spouses and certain direct descendants of such veterans, eligibility for certain housing loans and educational assistance administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAfrican Americans played a pivotal role in the war effort during World War II, with more than 1,200,000 African Americans serving in the Armed Forces, and, by 1945, approximately 1.9 percent of all officers in the Armed Forces were African Americans.\n**(2)**\nFollowing World War II, the Servicemen\u2019s Readjustment Act of 1944 (58 Stat. 284, commonly known as the GI Bill ) offered substantial material benefits to 16,000,000 veterans to assist them in reintegrating into civil society.\n**(3)**\nThe GI Bill offered a range of economic and educational benefits administered by the Federal Government through the Secretary of the Veterans Administration, including monetary assistance to access higher education, government guarantees for housing loans, unemployment allowances, and civilian workforce reentry assistance.\n**(4)**\nThough the legislative text of the GI Bill was race neutral, the administration of benefits through national, State, and local Veterans Administration offices resulted in a pattern of discrimination against racial minorities, especially African Americans.\n**(5)**\nVeterans Administration benefits counselors denied African Americans access to educational benefits at certain universities and funneled applicants into industrial and vocational schools rather than higher education opportunities, with just 6 percent of African-American veterans of World War II earning a college degree, compared to 19 percent of White veterans of World War II.\n**(6)**\nIn administering its housing guaranty program, the Veterans Administration adopted the Federal Housing Administration\u2019s racial exclusion programs, also known as redlining, which excluded a significant number of African Americans from taking full advantage of the housing guaranty program.\n**(7)**\nThe GI Bill created substantial economic growth and wealth accumulation for those who could benefit, but discriminatory administration of the program prevented many African-American veterans of World War II from enjoying the full economic prosperity of the post-war period.\n#### 3. Housing loans guaranteed by the Secretary of Veterans Affairs for Black veterans of World War II and survivors and certain direct descendants of such veterans\n##### (a) Establishment\nChapter 37 of title 38, United States Code, is amended as follows:\n**(1) Definition**\nSection 3701(b) of such title is amended by adding at the end the following new paragraphs:\n(8) The term veteran also includes, for purposes of housing loans, an individual who\u2014 (A) is Black; (B) served on active duty as a member of the Armed Forces during World War II; and (C) certifies to the Secretary that such individual was denied a specific benefit under the Servicemen's Readjustment Act of 1944 (58 Stat. 284) on the basis of race. (9) The term veteran also includes, for purposes of housing loans, an individual who\u2014 (A) is the surviving spouse, child, grandchild, or other direct descendant of a veteran described in paragraph (8); (B) certifies to the Secretary that such veteran described in paragraph (8) was denied a specific benefit under the Servicemen's Readjustment Act of 1944 (58 Stat. 284) on the basis of race; and (C) is living on the date of the enactment of the Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025 . .\n**(2) Basic entitlement**\nSection 3702(a)(2)(E) of such title is amended by adding at the end the following new subparagraph:\n(H) Each individual\u2014 (i) described in paragraph (8) or (9) of section 3701(b) of this title; and (ii) who applies for a housing loan during the five-year period beginning on the date of the enactment of the Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025 . .\n##### (b) Deadline\nThe Secretary shall carry out the amendment made by this section not later than 90 days after the date of the enactment of this Act.\n##### (c) Regulations\nThe Secretary of Veterans Affairs shall prescribe regulations to carry out the amendments made by this section.\n##### (d) GAO report\nNot later than one year after the deadline under subsection (b), the Comptroller General of the United States shall submit to Congress a report regarding\u2014\n**(1)**\nthe number of individuals who received housing loan benefits pursuant to the amendments made by this section; and\n**(2)**\nthe total value of housing loan benefits administered by the Secretary pursuant to the amendments made by this section.\n#### 4. Educational assistance for survivors and certain direct descendants of Black veterans of World War II\n##### (a) Entitlement\nSubsection (b) of section 3311 of title 38, United States Code, is amended by adding at the end the following new paragraph:\n(12) An individual\u2014 (A) described in section 3701(b)(9) of this title; and (B) who applies for educational assistance under this chapter during the five-year period beginning on the date of the enactment of the Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025 . .\n##### (b) Deadline\nThe Secretary shall carry out the amendment made by this section not later than 90 days after the date of the enactment of this Act.\n##### (c) Regulations\nThe Secretary of Veterans Affairs shall prescribe regulations to carry out the amendment made by this section.\n##### (d) GAO report\nNot later than one year after the deadline under subsection (b), the Comptroller General of the United States shall submit to Congress a report regarding\u2014\n**(1)**\nthe number of individuals who received educational assistance pursuant to the amendment made by this section; and\n**(2)**\nthe total amount of educational assistance paid by the Secretary pursuant to the amendment made by this section.\n#### 5. Blue Ribbon panel on benefits and assistance for female and minority veterans\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Veterans Affairs shall, pursuant to the Federal Advisory Committee Act ( Public Law 92\u2013463 ; 5 U.S.C. App.), appoint a panel of independent experts on\u2014\n**(1)**\ninequities in the distribution of benefits and assistance administered by the Secretary; and\n**(2)**\nmilitary service by female and minority members of the Armed Forces.\n##### (b) Duties\nThe panel shall develop recommendations regarding additional benefits and assistance for individuals described in subsection (a)(2), and related legislation.\n##### (c) Report\nNot later than one year after the date of the enactment of this Act, the panel shall submit to Congress and the President a report containing the recommendations developed under this section.",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-09-02T19:13:32Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-09-02T19:13:32Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-09-02T19:13:32Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Minority employment",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-09-02T19:13:31Z"
          },
          {
            "name": "Women's employment",
            "updateDate": "2025-09-02T19:13:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-25T18:00:27Z"
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
          "measure-id": "id119hr1725",
          "measure-number": "1725",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1725v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 GI bill benefits and the Department of Veterans Affairs (VA) home loan program by updating terminology related to certain Black veterans. Specifically, the bill explicitly includes the following individuals as eligible veterans under the programs:</p><ul><li>Black veterans who served on active duty during World War II and can certify they were denied a specific benefit on the basis of race; and</li><li>the living surviving spouses, children, grandchildren, or other direct descendants of such veterans described above who can certify the veteran was denied a specific benefit on the basis of race.</li></ul><p>Eligible veterans must apply for educational or home loan benefits within the five-year period after the bill is enacted.</p><p>The Government Accountability Office must report on the number of individuals who received VA educational or housing loan benefits due to the amendments made by the bill and the total value of such benefits.</p><p>Finally, the VA must appoint a panel of independent experts to develop recommendations regarding additional benefits and assistance for female and minority members of the Armed Forces.</p>"
        },
        "title": "Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1725.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 GI bill benefits and the Department of Veterans Affairs (VA) home loan program by updating terminology related to certain Black veterans. Specifically, the bill explicitly includes the following individuals as eligible veterans under the programs:</p><ul><li>Black veterans who served on active duty during World War II and can certify they were denied a specific benefit on the basis of race; and</li><li>the living surviving spouses, children, grandchildren, or other direct descendants of such veterans described above who can certify the veteran was denied a specific benefit on the basis of race.</li></ul><p>Eligible veterans must apply for educational or home loan benefits within the five-year period after the bill is enacted.</p><p>The Government Accountability Office must report on the number of individuals who received VA educational or housing loan benefits due to the amendments made by the bill and the total value of such benefits.</p><p>Finally, the VA must appoint a panel of independent experts to develop recommendations regarding additional benefits and assistance for female and minority members of the Armed Forces.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1725"
    },
    "title": "Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025</strong></p><p>This bill expands eligibility for Post-9/11 GI bill benefits and the Department of Veterans Affairs (VA) home loan program by updating terminology related to certain Black veterans. Specifically, the bill explicitly includes the following individuals as eligible veterans under the programs:</p><ul><li>Black veterans who served on active duty during World War II and can certify they were denied a specific benefit on the basis of race; and</li><li>the living surviving spouses, children, grandchildren, or other direct descendants of such veterans described above who can certify the veteran was denied a specific benefit on the basis of race.</li></ul><p>Eligible veterans must apply for educational or home loan benefits within the five-year period after the bill is enacted.</p><p>The Government Accountability Office must report on the number of individuals who received VA educational or housing loan benefits due to the amendments made by the bill and the total value of such benefits.</p><p>Finally, the VA must appoint a panel of independent experts to develop recommendations regarding additional benefits and assistance for female and minority members of the Armed Forces.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hr1725"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1725ih.xml"
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
      "title": "Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sgt. Isaac Woodard, Jr. and Sgt. Joseph H. Maddox GI Bill Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to extend to Black veterans of World War II, and surviving spouses and certain direct descendants of such veterans, eligibility for certain housing loans and educational assistance administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:21Z"
    }
  ]
}
```
