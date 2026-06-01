# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4704
- Title: ROTOR Act
- Congress: 119
- Bill type: HR
- Bill number: 4704
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-12T09:07:17Z
- Update date including text: 2025-12-12T09:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4704",
    "number": "4704",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001218",
        "district": "7",
        "firstName": "Richard",
        "fullName": "Rep. McCormick, Richard [R-GA-7]",
        "lastName": "McCormick",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "ROTOR Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:17Z",
    "updateDateIncludingText": "2025-12-12T09:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:16:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NE"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CO"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TX"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NV"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CO"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4704\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Mr. McCormick (for himself, Mr. Deluzio , Mr. Pfluger , Mr. Davis of North Carolina , Mr. Wittman , Mr. Moulton , Mrs. Kiggans of Virginia , Mr. Bacon , Mr. Khanna , Mr. McCaul , Mr. Golden of Maine , and Mr. Finstad ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Director of the Defense Health Agency to conduct a study on the prevalence and mortality of cancer among military rotary wing pilots and aviation support personnel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rotary-wing Operator Toxic Occupational Research Act or the ROTOR Act .\n#### 2. Study on prevalence and mortality of cancer among military rotary-wing pilots and aviation support personnel\n##### (a) Study required\nThe Director of the Defense Health Agency, in coordination with the Directors of the National Institutes of Health and the National Cancer Institute, shall conduct a study among covered individuals in two phases as provided by this section.\n##### (b) Initial phase of study\n**(1) Goal of initial phase**\nUnder the initial phase of the study under subsection (a), the Director of the Defense Health Agency shall determine, for each cancer specified in paragraph (2), whether there is an increased prevalence of, or increased rate of mortality caused by, such cancer for covered individuals as compared to similarly aged individuals in the general population (or, in the case of the cancer specified in paragraph (2)(B), for female covered individuals as compared to similarly aged women in the general population).\n**(2) Cancers specified**\nThe cancers specified in this paragraph are the following:\n**(A)**\nBrain cancer.\n**(B)**\nBreast cancer.\n**(C)**\nColon and rectal cancer.\n**(D)**\nKidney cancer.\n**(E)**\nLung cancer.\n**(F)**\nMelanoma.\n**(G)**\nNon-Hodgkin\u2019s lymphoma.\n**(H)**\nOvarian cancer.\n**(I)**\nPancreatic cancer.\n**(J)**\nProstate cancer.\n**(K)**\nTesticular cancer.\n**(L)**\nUrinary bladder cancer.\n**(3) Report on initial phase**\nNot later than one year after the date of the enactment of this Act, the Director of the Defense Health Agency shall submit to the appropriate congressional committees a report on the findings of the phase of the study under this subsection.\n##### (c) Second phase of study\n**(1) Goal of second phase**\nIf, pursuant to the phase of the study under subsection (b), the Director of the Defense Health Agency determines there is an increased prevalence of, or increased mortality rate caused by, any cancer specified in subsection (b)(2) among covered individuals (or, with respect to the cancer specified in subsection (b)(2)(B), among female covered individuals), the Director shall conduct a second phase of the study to\u2014\n**(A)**\nidentify any carcinogenic toxin or other hazardous material associated with the operation of military rotary-wing aircraft, such as fumes, fuels, or other liquids;\n**(B)**\nidentify any operating environment, including frequencies or electromagnetic fields, in which covered individuals may have received excess exposure to non-ionizing radiation in the course of such operation, including non-ionizing radiation associated with airborne, ground, or shipboard radars; and\n**(C)**\nidentify potential exposures as a result of military service by covered individuals to carcinogenic toxins or other hazardous materials not associated with the operation of military rotary-wing aircraft (such as exposure to burn pits, toxins in contaminated water, or toxins embedded in soils), including by determining\u2014\n**(i)**\nthe locations of such service; and\n**(ii)**\nany duties of covered individuals unrelated to such operation and associated with an increased prevalence of, or increased mortality rate caused by, cancer.\n**(2) Report on second phase**\nIf the Director of the Defense Health Agency conducts the phase of the study under this subsection, not later than one year after the date on which the Director submits the report under subsection (b)(3), the Director shall submit to the appropriate congressional committees a report on the findings of such phase.\n**(3) Data format**\nThe Director of the Defense Health Agency shall format any data resulting from the phase of the study under this subsection consistent with the formatting of data under the Surveillance, Epidemiology, and End Results program, including by disaggregating such data by race, gender, and age.\n##### (d) Sources of data\nIn conducting the study under this section, the Director of the Defense Health Agency shall use data from\u2014\n**(1)**\nthe database of the Surveillance, Epidemiology, and End Results program;\n**(2)**\nthe study conducted under section 750 of the National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 134 Stat. 3716); and\n**(3)**\nany other study previously conducted by the Secretary of a military department that the Director determines relevant for purposes of this section.\n##### (e) Definitions\nIn this section:\n**(1)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the Senate.\n**(2)**\nThe term covered Armed Force means the Army, Navy, Marine Corps, Air Force, or Space Force.\n**(3)**\nThe term covered individual means any individual who\u2014\n**(A)**\nserved in a covered Armed Force on or after February 28, 1961, as an aircrew member of a rotary-wing aircraft (including as a pilot or aviation support personnel), without regard to the status, position, rank, or grade of the individual within such crew; and\n**(B)**\nreceives health care benefits under chapter 55 of title 10, United States Code.\n**(4)**\nThe term Surveillance, Epidemiology, and End Results program means the program of the National Cancer Institute referred to in section 399B(d)(1) of the Public Health Service Act ( 40 U.S.C. 280e(d)(1) ), or any successor program.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-09-30",
        "text": "Received in the Senate."
      },
      "number": "3838",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Procurement for Effective Execution and Delivery and National Defense Authorization Act for Fiscal Year 2026",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-19T17:29:52Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4704ih.xml"
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
      "title": "ROTOR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-08T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ROTOR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rotary-wing Operator Toxic Occupational Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-08T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the Defense Health Agency to conduct a study on the prevalence and mortality of cancer among military rotary wing pilots and aviation support personnel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-08T04:48:36Z"
    }
  ]
}
```
