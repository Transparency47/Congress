# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/307?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/307
- Title: ARC Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 307
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-04-28T08:05:46Z
- Update date including text: 2026-04-28T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H122)
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-09 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-14 - IntroReferral: Sponsor introductory remarks on measure. (CR H122)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/307",
    "number": "307",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "ARC Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:05:46Z",
    "updateDateIncludingText": "2026-04-28T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H122)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:36:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-09T14:36:00Z",
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
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "IL"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "NJ"
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
      "sponsorshipDate": "2025-01-13",
      "state": "AL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "KS"
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
      "sponsorshipDate": "2025-01-13",
      "state": "GA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "MN"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-14",
      "state": "NY"
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
      "sponsorshipDate": "2025-01-14",
      "state": "NC"
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
      "sponsorshipDate": "2025-01-14",
      "state": "OH"
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
      "sponsorshipDate": "2025-01-14",
      "state": "MS"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-14",
      "state": "DC"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "MA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "AZ"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MN"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "FL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "GA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "GU"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "MD"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "TX"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "False",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "NY"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NC"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NJ"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "MI"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "VI"
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
      "sponsorshipDate": "2025-10-10",
      "state": "NC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr307ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 307\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mrs. McIver (for herself, Mr. Jackson of Illinois , and Ms. Kelly of Illinois ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XVIII and XIX of the Social Security Act to provide for coverage of peripheral artery disease screening tests furnished to at-risk beneficiaries under the Medicare and Medicaid programs without the imposition of cost-sharing requirements, and for other purposes.\n#### 1. Short title; findings\n##### (a) Short title\nThis Act may be cited as the Amputation Reduction and Compassion Act of 2025 or the ARC Act of 2025 .\n##### (b) Findings\nCongress makes the following findings:\n**(1)**\nAtherosclerosis occurs when blood flow is reduced because arteries become narrowed or blocked with fatty deposits.\n**(2)**\nAtherosclerosis is responsible for more deaths in the United States than any other condition, and heart attacks, resulting from clogged coronary arteries, are the leading cause of death in America.\n**(3)**\nAtherosclerosis also occurs in the legs and is known as peripheral artery disease (in this subsection referred to as PAD ) and having PAD significantly increases the risk for heart attack, stroke, amputation, and death.\n**(4)**\nWhile most Americans are aware of atherosclerosis in the heart, many Americans have never heard of PAD and Americans with PAD are often unaware of the serious risks of the disease.\n**(5)**\nAn estimated 21 million Americans have PAD, and about 200,000 of them\u2014disproportionately minorities\u2014suffer avoidable amputations every year as a result of such disease.\n**(6)**\nAccording to the Dartmouth Atlas, amputation risks for African Americans living with diabetes are as much as four times higher than the national average.\n**(7)**\nData analyses have similarly found that Native Americans are more than twice as likely to be subjected to amputation and Hispanics are up to 75 percent more likely to have an amputation.\n**(8)**\nFifty-two percent of patients with an above-the-knee amputation and 33 percent of patients with a below-the-knee amputation will die within two years of their amputation.\n**(9)**\nScreening and arterial testing for PAD is cost-effective and should be part of routine medical care.\n**(10)**\nOnce PAD is detected, amputations and deaths can be reduced through the use of national, evidence-based PAD care guidelines.\n**(11)**\nAmericans with a PAD diagnosis are associated with a 67-percent increase in the risk of cardiac death compared to people without a PAD diagnosis. Consequently, screening for PAD enables health care professionals to identify cardiac risk factors earlier and take proactive measures to reduce the risk of cardiac death.\n#### 2. Peripheral artery disease education program\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following new section:\n399V\u20138. Peripheral artery disease education program (a) Establishment The Secretary, acting through the Director of the Centers for Disease Control and Prevention, in collaboration with the Administrator of the Centers for Medicare & Medicaid Services, the Administrator of the Health Resources and Services Administration, leading clinical and patient advocacy organizations, and other interested stakeholders shall establish and coordinate a peripheral artery disease education program to support, develop, and implement educational initiatives and outreach strategies that inform health care professionals and the public about the existence of peripheral artery disease and methods to reduce amputations related to such disease, particularly with respect to at-risk populations. (b) Best practices The Secretary shall, as appropriate, identify and disseminate to health care professionals best practices with respect to peripheral artery disease. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section $6,000,000 for each of fiscal years 2026 through 2030. .\n#### 3. Medicare coverage of peripheral artery disease screening tests furnished to at-risk beneficiaries without imposition of cost-sharing requirements\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nin subparagraph (JJ), by striking the semicolon at the end and inserting ; and ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(KK) peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in subsection (nnn)). ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) Peripheral artery disease screening test; At-Risk beneficiary (1) The term peripheral artery disease screening test means\u2014 (A) noninvasive physiologic studies of extremity arteries (commonly referred to as ankle-brachial index testing); (B) arterial duplex scans of lower extremity arteries vascular; and (C) such other items and services as the Secretary determines, in consultation with relevant stakeholders, to be appropriate for screening for peripheral artery disease for at-risk beneficiaries. (2) The term at-risk beneficiary means an individual entitled to, or enrolled for, benefits under part A and enrolled for benefits under part B\u2014 (A) who is 65 years of age or older; (B) who is at least 50 years of age but not older than 64 years of age with risk factors for atherosclerosis (such as diabetes mellitus, a history of smoking, hyperlipidemia, and hypertension) or a family history of peripheral artery disease; (C) who is younger than 50 years of age with diabetes mellitus and one additional risk factor for atherosclerosis; or (D) with a known atherosclerotic disease in another vascular bed such as coronary, carotid, subclavian, renal, or mesenteric artery stenosis, or abdominal aortic aneurysm. (3) The Secretary shall, in consultation with appropriate organizations, establish standards regarding the frequency for peripheral artery disease screening tests described in subsection (s)(2)(KK) for purposes of coverage under this title. .\n##### (b) Inclusion of peripheral artery disease screening tests in initial preventive physical examination\nSection 1861(ww)(2) of the Social Security Act ( 42 U.S.C. 1395x(ww)(2) ) is amended\u2014\n**(1)**\nin subparagraph (N), by moving the margins of such subparagraph 2 ems to the left;\n**(2)**\nby redesignating subparagraph (O) as subparagraph (P); and\n**(3)**\nby inserting after subparagraph (N) the following new subparagraph:\n(O) Peripheral artery disease screening tests furnished to at risk-beneficiaries (as such terms are defined in subsection (nnn)). .\n##### (c) Payment\n**(1) In general**\nSection 1833(a) of the Social Security Act ( 42 U.S.C. 1395l(a) ) is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (N), by inserting and other than peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1861(nnn)) after other than personalized prevention plan services (as defined in section 1861(hhh)(1)) ;\n**(ii)**\nby striking and before (HH) ; and\n**(iii)**\nby adding at the end the following: and (II) with respect to peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1861(nnn)), the amount paid shall be 100 percent of the lesser of the actual charge for the services or the amount determined under the payment basis determined under section 1848; ; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (G), by striking and at the end;\n**(ii)**\nin subparagraph (H), by striking the semicolon at the end and inserting ; and ; and\n**(iii)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) with respect to peripheral artery disease screening tests (as defined in paragraph (1) of section 1861(nnn)) furnished by an outpatient department of a hospital to at-risk beneficiaries (as defined in paragraph (2) of such section), the amount determined under paragraph (1)(II); .\n**(2) No deductible**\nSection 1833(b) of the Social Security Act ( 42 U.S.C. 1395l(b) ) is amended, in the first sentence\u2014\n**(A)**\nby striking , and before (13) ; and\n**(B)**\nby inserting before the period at the end the following: , and (14) such deductible shall not apply with respect to peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1861(nnn)) .\n**(3) Exclusion from prospective payment system for hospital outpatient department services**\nSection 1833(t)(1)(B)(iv) of the Social Security Act ( 42 U.S.C. 1395l(t)(1)(B)(iv) ) is amended\u2014\n**(A)**\nby striking , or personalized and inserting , personalized ; and\n**(B)**\nby inserting , or peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1861(nnn)) after personalized prevention plan services (as defined in section 1861(hhh)(1)) .\n**(4) Conforming amendment**\nSection 1848(j)(3) of the Social Security Act ( 42 U.S.C. 1395w\u20134(j)(3) ) is amended by striking (2)(FF) (including administration of the health risk assessment), and inserting (2)(FF) (including administration of the health risk assessment), (2)(KK), .\n##### (d) Exclusion from coverage and Medicare as secondary payer for tests performed more frequently than allowed\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by striking the semicolon at the end and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1861(nnn)), which are performed more frequently than is covered under such section; .\n##### (e) Authority To modify or eliminate coverage of certain preventive services\nSection 1834(n) of the Social Security Act ( 42 U.S.C. 1395m(n) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) of paragraph (1) as clauses (i) and (ii), respectively, and moving the margins of such clauses, as so redesignated, 2 ems to the right;\n**(2)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B), respectively, and moving the margins of such subparagraphs, as so redesignated, 2 ems to the right;\n**(3)**\nby striking Certain Preventive Services and all that follows through any other provision of this title and inserting:\nCertain Preventive Services.\u2014 (1) In general Notwithstanding any other provision of this title ; and\n**(4)**\nby adding at the end the following new paragraph:\n(2) Inapplicability The Secretarial authority described in paragraph (1) shall not apply with respect to preventive services described in section 1861(ww)(2)(O). .\n##### (f) Effective date\nThe amendments made by this section shall apply with respect to items and services furnished on or after January 1, 2026.\n#### 4. Medicaid coverage of peripheral artery disease screening tests furnished to at-risk beneficiaries without imposition of cost-sharing requirements\n##### (a) In general\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (31), by striking and at the end;\n**(B)**\nby redesignating paragraph (32) as paragraph (33); and\n**(C)**\nby inserting after paragraph (31) the following new paragraph:\n(32) peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in subsection (kk)); and ; and\n**(2)**\nby adding at the end the following new subsection:\n(kk) Peripheral artery disease screening test; At-Risk beneficiary (1) Peripheral artery disease screening test The term peripheral artery disease screening test means\u2014 (A) noninvasive physiologic studies of extremity arteries (commonly referred to as ankle-brachial index testing); (B) arterial duplex scans of lower extremity arteries vascular; and (C) such other items and services as the Secretary determines, in consultation with relevant stakeholders, to be appropriate for screening for peripheral artery disease for at-risk beneficiaries. (2) At-risk beneficiary The term at-risk beneficiary means an individual enrolled under a State plan (or a waiver of such plan)\u2014 (A) who is 65 years of age or older; (B) who is at least 50 years of age but not older than 64 years of age with risk factors for atherosclerosis (such as diabetes mellitus, a history of smoking, hyperlipidemia, and hypertension) or a family history of peripheral artery disease; (C) who is younger than 50 years of age with diabetes mellitus and one additional risk factor for atherosclerosis; or (D) with a known atherosclerotic disease in another vascular bed such as coronary, carotid, subclavian, renal, or mesenteric artery stenosis, or abdominal aortic aneurysm. (3) Frequency The Secretary shall, in consultation with appropriate organizations, establish standards regarding the frequency for peripheral artery disease screening tests described in subsection (a)(31) for purposes of coverage under a State plan under this title. .\n##### (b) No cost sharing\n**(1) In general**\nSubsections (a)(2) and (b)(2) of section 1916 of the Social Security Act ( 42 U.S.C. 1396o ) are each amended\u2014\n**(A)**\nin subparagraph (I), by striking or at the end;\n**(B)**\nin subparagraph (J), by striking ; and and inserting , or ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(K) peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1905(kk)); and .\n**(2) Application to alternative cost sharing**\nSection 1916A(b)(3)(B) of the Social Security Act ( 42 U.S.C. 1396o\u20131(b)(3)(B) ) is amended by adding at the end the following new clause:\n(xv) Peripheral artery disease screening tests furnished to at-risk beneficiaries (as such terms are defined in section 1905(kk)). .\n##### (c) Conforming amendments\n**(1)**\nSection 1902(nn)(3) of the Social Security Act ( 42 U.S.C. 1396a(nn)(3) ) is amended by striking following paragraph (31) and inserting following paragraph (32) .\n**(2)**\nSection 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) ) is amended by striking following paragraph (31) and inserting following paragraph (32) .\n#### 5. Development and implementation of quality measures\n##### (a) Development\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall, in consultation with relevant stakeholders, develop quality measures for nontraumatic, lower-limb, major amputation that utilize appropriate diagnostic screening (including peripheral artery disease screening) in order to encourage alternative treatments (including revascularization) in lieu of such an amputation.\n##### (b) Implementation\nNot later than 18 months after the date of enactment of this Act, the Secretary shall complete appropriate testing and validation of the measures developed under subsection (a) and shall incorporate such measures in quality reporting programs for appropriate providers of services and suppliers under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), including for purposes of\u2014\n**(1)**\nthe merit-based incentive payment system under section 1848(q) of such Act ( 42 U.S.C. 1395w\u20134(q) );\n**(2)**\nincentive payments for participation in eligible alternative payment models under section 1833(z) of such Act ( 42 U.S.C. 1395l(z) );\n**(3)**\nthe shared savings program under section 1899 of such Act ( 42 U.S.C. 1395jjj );\n**(4)**\nmodels under section 1115A of such Act ( 42 U.S.C. 1315a ); and\n**(5)**\nsuch other payment systems or models as the Secretary may specify.\n#### 6. Amputation prevention pilot program\n##### (a) In general\nSection 1115A(b)(2)(B) of the Social Security Act ( 42 U.S.C. 1315a(b)(2)(B) ) is amended by adding at the end the following new clause:\n(xxviii) Promoting voluntary, nontraumatic lower-limb major amputation prevention programs at hospitals, ambulatory surgical centers, and office-based centers that will increase access to amputation prevention services, reduce amputation rates, and reduce costs to such hospitals, surgical centers, and office-based centers, through\u2014 (I) patient risk modification and management; (II) early screening and detection and surveillance; (III) testing and treatment for peripheral artery disease; and (IV) improved care coordination for individuals at high risk for amputation. .\n##### (b) Testing of model\nNot later than 18 months after the date of the enactment of this Act, the Deputy Administrator and Director of the Center for Medicare and Medicaid Innovation shall test the model described under subsection (a).",
      "versionDate": "2025-01-09",
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
            "name": "Cardiovascular and respiratory health",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Digestive and metabolic diseases",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Education programs funding",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Health technology, devices, supplies",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Home and outpatient care",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Insurance industry and regulation",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-02-10T19:03:05Z"
          },
          {
            "name": "Surgery and anesthesia",
            "updateDate": "2025-02-10T19:03:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-06T19:49:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr307",
          "measure-number": "307",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr307v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Amputation Reduction and Compassion Act of 2025\u00a0or the ARC Act of </strong><strong>2025\u00a0</strong></p><p>This bill provides for coverage of peripheral artery disease screening tests without cost-sharing under Medicare and Medicaid for certain at-risk individuals. It also requires the development of certain educational programs, a payment model, and Medicare quality measures to reduce amputations relating to such disease.</p>"
        },
        "title": "ARC Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr307.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Amputation Reduction and Compassion Act of 2025\u00a0or the ARC Act of </strong><strong>2025\u00a0</strong></p><p>This bill provides for coverage of peripheral artery disease screening tests without cost-sharing under Medicare and Medicaid for certain at-risk individuals. It also requires the development of certain educational programs, a payment model, and Medicare quality measures to reduce amputations relating to such disease.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr307"
    },
    "title": "ARC Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Amputation Reduction and Compassion Act of 2025\u00a0or the ARC Act of </strong><strong>2025\u00a0</strong></p><p>This bill provides for coverage of peripheral artery disease screening tests without cost-sharing under Medicare and Medicaid for certain at-risk individuals. It also requires the development of certain educational programs, a payment model, and Medicare quality measures to reduce amputations relating to such disease.</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr307"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr307ih.xml"
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
      "title": "ARC Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:06Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ARC Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Amputation Reduction and Compassion Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XVIII and XIX of the Social Security Act to provide for coverage of peripheral artery disease screening tests furnished to at-risk beneficiaries under the Medicare and Medicaid programs without the imposition of cost-sharing requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T04:33:37Z"
    }
  ]
}
```
