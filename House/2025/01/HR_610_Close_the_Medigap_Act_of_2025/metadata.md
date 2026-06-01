# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/610
- Title: Close the Medigap Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 610
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-02-04T09:07:13Z
- Update date including text: 2026-02-04T09:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-22 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/610",
    "number": "610",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Close the Medigap Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T09:07:13Z",
    "updateDateIncludingText": "2026-02-04T09:07:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-22T15:05:00Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IN"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CT"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MI"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "AZ"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "WA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "OH"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "DC"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NJ"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "MD"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "AL"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "WI"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr610ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 610\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Doggett (for himself, Mr. Bishop , Mr. Carson , Mr. Casar , Mr. Casten , Ms. Chu , Mr. Cleaver , Mr. Cohen , Ms. DeLauro , Mrs. Dingell , Mr. Espaillat , Mrs. Fletcher , Mr. Garamendi , Ms. Garcia of Texas , Mr. Grijalva , Ms. Jayapal , Mr. Johnson of Georgia , Ms. Kaptur , Mr. Khanna , Ms. Lee of Pennsylvania , Ms. Norton , Ms. Ocasio-Cortez , Ms. Pressley , Mrs. Ramirez , Ms. Schakowsky , Mr. Sherman , Mr. Takano , Mr. Tonko , Mr. Veasey , Mrs. Watson Coleman , Ms. Williams of Georgia , and Mr. Garc\u00eda of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide for certain reforms with respect to medicare supplemental health insurance policies.\n#### 1. Short title\nThis Act may be cited as the Close the Medigap Act of 2025 .\n#### 2. Guaranteed issue\n##### (a) In general\nSection 1882(s) of the Social Security Act ( 42 U.S.C. 1395ss(s) ) is amended to read as follows:\n(s) (1) Subject to paragraph (2), the issuer of a medicare supplemental policy may not, in the case of an individual entitled to benefits under part A and enrolled under part B\u2014 (A) deny or condition the issuance or effectiveness of a medicare supplemental policy, or discriminate in the pricing of the policy, because of health status, claims experience, receipt of health care, or medical condition; (B) exclude benefits based on a preexisting condition; (C) provide any time period applicable to preexisting conditions, waiting periods, elimination periods, and probationary periods for any benefit; (D) deny or condition the issuance or effectiveness of the policy (including the imposition of any exclusion of benefits under the policy based on a preexisting condition) or discriminate in the pricing of the policy (including the adjustment of premium rates) of an individual on the basis of the genetic information with respect to such individual; (E) deny or condition the issuance or effectiveness of a medicare supplemental policy that is offered and is available for issuance to new enrollees by such issuer; or (F) establish any period limiting enrollment under a medicare supplemental policy to such period for any individual. (2) Paragraph (1) shall not apply to an individual entitled to benefits under part A solely by reason of section 226A. (3) Nothing in this subsection or in subparagraph (A) or (B) of subsection (x)(2) shall be construed to limit the ability of an issuer of a medicare supplemental policy from, to the extent otherwise permitted under this title\u2014 (A) denying or conditioning the issuance or effectiveness of the policy or increasing the premium for an employer based on the manifestation of a disease or disorder of an individual who is covered under the policy; or (B) increasing the premium for any policy issued to an individual based on the manifestation of a disease or disorder of an individual who is covered under the policy (in such case, the manifestation of a disease or disorder in one individual cannot also be used as genetic information about other group members. .\n##### (b) Outreach plan\n**(1) In general**\nThe Secretary of Health and Human Services shall develop an outreach plan to notify individuals entitled to benefits under part A or enrolled under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ) of the effects of the amendment made by subsection (a).\n**(2) Consultation**\nIn implementing the outreach plan developed under paragraph (1), the Secretary shall consult with consumer advocates, brokers, insurers, the National Association of Insurance Commissioners, and State Health Insurance Assistance Programs.\n##### (c) Effective date; phase-In authority\n**(1) Effective date**\nSubject to paragraph (2), the amendment made by subsection (a) shall apply to medicare supplemental policies effective on or after January 1, 2026.\n**(2) Phase-in authority**\n**(A) In general**\nSubject to subparagraph (B), the Secretary of Health and Human Services may phase in the implementation of the amendment made under subsection (a) (with such phase-in beginning on or after January 1, 2026) in such manner as the Secretary determines appropriate in order to minimize any adverse impact on individuals enrolled under a medicare supplemental policy.\n**(B) Phase-in period may not exceed 5 years**\nThe Secretary of Health and Human Services shall ensure that the amendment made by subsection (a) is fully implemented by not later than January 1, 2031.\n#### 3. Medical loss ratio\nSection 1882(r)(1)(A) of the Social Security Act ( 42 U.S.C. 1395ss(r)(1)(A) ) is amended\u2014\n**(1)**\nby inserting and periodically reviewed after developed ; and\n**(2)**\nby striking policy, at least 75 percent of the aggregate amount of premiums collected in the case of group policies and at least 65 percent in the case of individual policies; and and inserting the following:\npolicy\u2014 (i) with respect to periods beginning before January 1, 2026, at least 75 percent of the aggregate amount of premiums collected in the case of group policies and at least 65 percent in the case of individual policies; and (ii) with respect to periods beginning on or after January 1, 2026, a percent of the aggregate amount of premiums collected that, in the case of group policies or individual policies, as applicable, is equal to or greater than both\u2014 (I) the applicable percent specified in clause (i) with respect to such policies; and (II) such percent as the National Association of Insurance Commissioners may recommend to the Secretary with respect to such policies for purposes of this paragraph; and .\n#### 4. Limitations on pricing discrimination\n##### (a) In general\nSection 1882 of the Social Security Act ( 42 U.S.C. 1395ss ), as amended by section 6, is further amended by adding at the end the following new subsection:\n(aa) Development of new standards relating to pricing discrimination (1) In general The Secretary shall request the National Association of Insurance Commissioners to review and revise the standards for all benefit packages under subsection (p)(1), including the core benefit package, in order to provide coverage consistent with paragraph (2). Such revisions shall be made consistent with the rules applicable under subsection (p)(1)(E) (with the reference to the 1991 NAIC Model Regulation deemed a reference to the NAIC Model Regulation as most recently updated by the National Association of Insurance Commissioners to reflect previous changes in law and the reference to date of enactment of this subsection deemed a reference to the date of enactment of this subsection). (2) Changes in cost-sharing described Under the revised standards, coverage shall not be available under a Medicare supplemental insurance policy unless the issuer of the policy, in addition to conforming to the other applicable requirements of this section\u2014 (A) does not discriminate in the pricing of the policy because of the age of the individual to whom the policy is issued; (B) does not, to an extent that jeopardizes the access to such policy for individuals who are eligible to participate in the program under this title because the individuals are individuals described in paragraph (2) or (3) of section 1811, discriminate in the pricing of the policy because the individual to whom the policy is issued is so eligible to participate in such program because the individual is an individual so described in such a paragraph; and (C) does not establish premiums applicable under such policy on a basis that would apply to a portion of, but not the entirety of, a county or equivalent area specified by the Secretary. (3) Application date The revised standards shall apply to benefit packages sold, issued, or renewed under this section to individuals who first become entitled to benefits under part A or first enrolls in part B on or after January 1, 2026. .\n##### (b) Conforming amendment\nSection 1882(o)(1) of such Act ( 42 U.S.C. 1395ss(o)(1) ) is amended by striking , and (y) and inserting (y), and (aa) .\n#### 5. Clarifying beneficiary options on the Medicare plan finder website\nSection 1804 of the Social Security Act ( 42 U.S.C. 1395b\u20132 ) is amended by adding at the end the following new subsections:\n(d) In the case that the Secretary provides for a Medicare plan finder internet website of the Centers for Medicare & Medicaid Services (or a successor website), the Secretary shall, with respect to such website and in accordance with subsection (f)\u2014 (1) make available on such website\u2014 (A) access to provider networks in order to provide to individuals entitled to benefits under part A or enrolled under part B information to assist such individuals in understanding the restrictions on providers and potential costs entailed by their decisions regarding enrollment under parts A and B, under part C, and in medicare supplemental policies under section 1882; (B) a review of out-of-pocket expenditures, including deductibles, copayments, coinsurance, monthly premiums, and estimated annual out-of-pocket costs, displayed overall and by components, based on the best available information as determined by the Secretary; and (C) during the period prior to January 1, 2026, information regarding the rules that, in each State, pertain to guaranteed issue of medicare supplemental health insurance policies prior to implementation of the provisions of the Close the Medigap Act of 2025 and, in the case that a State has no such rules pertaining to guaranteed issue of such policies, clear language explaining the implications of such lack of rules for individuals with pre-existing conditions; (2) not later than January 1, 2026, and periodically thereafter, perform a review of such website in order to ensure that such website makes available to individuals entitled to benefits under part A or enrolled under part B the information that the Secretary determines is necessary for such individuals to make informed choices regarding their options under the program under this title; and (3) not later than 12 months after the last day of each period for the request for information under subsection (e), update such website, taking into consideration the information collected pursuant to such subsection, to clarify the presentation of consumer options for medicare supplemental health insurance policy options, including by presenting such information in a manner calculated to be understood by the average consumer and in a manner that\u2014 (A) improves consumer access to information regarding the applicable premiums under such policy options as of the date on which such website is so updated; (B) facilitates consumers\u2019 ability to compare and sort policy options and premium information across plan offerings in a given location; (C) clarifies and explains differences in policy value; (D) rates and explains the financial stability of issuers of such policies; (E) provides data on the inflation rate of different policies; (F) provides information regarding the guaranteed issue requirements that apply to medicare supplemental health insurance policies under section 1882(s)(3); and (G) includes such general information as is determined by the Secretary to be necessary for individuals entitled to benefits under part A or enrolled under part B to understand costs under MA plans available pursuant to part C and prescription drug plans available pursuant to part D. (e) Not later than 6 months after the date of the enactment of this subsection and beginning on December 7 of each year thereafter, the Secretary of Health and Human Services shall provide an opportunity for public comment during which the Secretary requests information, including recommendations, from stakeholders regarding potential improvements to the presentation of medicare supplemental health insurance policy options under section 1882 on the Medicare plan finder internet website of the Centers for Medicare & Medicaid Services (or a successor website). (f) With respect to any information that the Secretary makes available on the Medicare plan finder internet website of the Centers for Medicare & Medicaid Services (or a successor website) pursuant to subsection (d), the Secretary shall, prior to making such information available\u2014 (1) provide, in consultation with the National Association of Insurance Commissioners, an opportunity for consumer testing of such information; (2) share the results of such consumer testing of such information with interested stakeholders; and (3) provide a 60-day public comment period with respect to such information. .\n#### 6. Restoring access to first-dollar Medigap coverage\nSection 1882 of the Social Security Act ( 42 U.S.C. 1395ss ) is amended by striking subsection (z).\n#### 7. Broker transparency\nSection 1128G of the Social Security Act ( 42 U.S.C. 1320a\u20137h ) is amended\u2014\n**(1)**\nin subsection (c)(1)(A), by striking 2011, and inserting 2011 (or, with respect to information required to be submitted under subsection (f)(1), not later than six months after the date of the enactment of such subsection), ; and\n**(2)**\nby adding at the end the following new subsection:\n(f) Application to Medigap insurance brokers (1) In general Beginning not later than 12 months after the date of enactment of this subsection, each issuer of a medicare supplemental health insurance policy shall annually submit to the Secretary a report regarding payments or other transfers of value made during the previous year to agents, brokers, and other third parties representing such policy. Each such report shall include the following information, with respect to such a payment or other transfer of value: (A) The name of the recipient of the payment or other transfer of value. (B) The business address of the recipient. (C) The amount of the payment or other transfer of value. (D) The dates on which the payment or transfer of value was provided. (E) A description of the form of the payment or transfer of value. (F) Any other categories of information the Secretary determines appropriate. (2) Application of transparency system The provisions of subsections (b) through (d) shall apply to an issuer described in paragraph (1), information required to be reported under such paragraph, and agents, brokers, and other third parties described in such paragraph in the same manner and to the same extent as such provisions apply to an applicable manufacturer, information required to be reported under subsection (a), and a covered recipient. .",
      "versionDate": "2025-01-22",
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
            "name": "Government information and archives",
            "updateDate": "2025-03-03T18:10:01Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-03T18:10:01Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-03T18:10:01Z"
          },
          {
            "name": "Insurance industry and regulation",
            "updateDate": "2025-03-03T18:10:01Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-03-03T18:10:01Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-03-03T18:10:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T20:22:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr610",
          "measure-number": "610",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr610v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Close the Medigap Act of 2025</strong><strong></strong></p><p>This bill (1) expands guaranteed issue rights with respect to Medigap policies (Medicare supplemental health insurance policies), (2) eliminates certain limitations\u00a0on Medigap policies for newly eligible Medicare beneficiaries, and (3) modifies other provisions related to Medigap policies. (Guaranteed issue rights require that a policy be offered to any eligible applicant without regard to health status.)</p>"
        },
        "title": "Close the Medigap Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr610.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Close the Medigap Act of 2025</strong><strong></strong></p><p>This bill (1) expands guaranteed issue rights with respect to Medigap policies (Medicare supplemental health insurance policies), (2) eliminates certain limitations\u00a0on Medigap policies for newly eligible Medicare beneficiaries, and (3) modifies other provisions related to Medigap policies. (Guaranteed issue rights require that a policy be offered to any eligible applicant without regard to health status.)</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr610"
    },
    "title": "Close the Medigap Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Close the Medigap Act of 2025</strong><strong></strong></p><p>This bill (1) expands guaranteed issue rights with respect to Medigap policies (Medicare supplemental health insurance policies), (2) eliminates certain limitations\u00a0on Medigap policies for newly eligible Medicare beneficiaries, and (3) modifies other provisions related to Medigap policies. (Guaranteed issue rights require that a policy be offered to any eligible applicant without regard to health status.)</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr610"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr610ih.xml"
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
      "title": "Close the Medigap Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-21T06:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Close the Medigap Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T06:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide for certain reforms with respect to medicare supplemental health insurance policies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T06:49:30Z"
    }
  ]
}
```
