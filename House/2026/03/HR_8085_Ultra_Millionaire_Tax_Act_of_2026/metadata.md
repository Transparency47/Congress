# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8085?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8085
- Title: Ultra-Millionaire Tax Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8085
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-05-13T08:06:47Z
- Update date including text: 2026-05-13T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8085",
    "number": "8085",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "J000298",
        "district": "7",
        "firstName": "Pramila",
        "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
        "lastName": "Jayapal",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Ultra-Millionaire Tax Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:47Z",
    "updateDateIncludingText": "2026-05-13T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:01:15Z",
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
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NC"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
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
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AZ"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
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
      "sponsorshipDate": "2026-03-25",
      "state": "GA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
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
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MN"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NM"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "HI"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
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
      "sponsorshipDate": "2026-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-02",
      "state": "PA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "ME"
    },
    {
      "bioguideId": "M001246",
      "district": "11",
      "firstName": "Analilia",
      "fullName": "Rep. Mejia, Analilia [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Mejia",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "NJ"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "CA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8085ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8085\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Ms. Jayapal (for herself, Mr. Boyle of Pennsylvania , Ms. Ansari , Mr. Beyer , Ms. Chu , Mr. Davis of Illinois , Ms. Dean of Pennsylvania , Mr. Deluzio , Mr. DeSaulnier , Mrs. Foushee , Ms. Friedman , Mr. Frost , Mr. Garc\u00eda of Illinois , Mr. Garcia of California , Mr. Goldman of New York , Mrs. Grijalva , Mr. Ivey , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Kelly of Illinois , Ms. Lee of Pennsylvania , Mr. McGovern , Mr. Nadler , Ms. Norton , Ms. Ocasio-Cortez , Ms. Omar , Mr. Pallone , Ms. Pressley , Mrs. Ramirez , Ms. S\u00e1nchez , Ms. Schakowsky , Ms. Simon , Mr. Smith of Washington , Ms. Stansbury , Mr. Takano , Mr. Thanedar , Ms. Tlaib , Ms. Tokuda , Ms. Vel\u00e1zquez , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose a tax on the net value of assets of a taxpayer, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ultra-Millionaire Tax Act of 2026 .\n#### 2. Imposition of wealth tax\n##### (a) In general\nThe Internal Revenue Code of 1986 is amended by inserting after subtitle B the following new subtitle:\nB\u20131 Wealth tax Chapter 18\u2014Determination of wealth tax 18 Determination of wealth tax Sec. 2901. Imposition of tax. Sec. 2902. Net value of taxable assets. Sec. 2903. Special rules. Sec. 2904. Information reporting. Sec. 2905. Enforcement. 2901. Imposition of tax (a) In general In the case of an individual, a tax is hereby imposed on the net value of all taxable assets of the taxpayer on the last day of any calendar year. (b) Computation of tax (1) In general The tax imposed by this section shall be equal to the sum of\u2014 (A) 0 percent of so much of the net value of all taxable assets of the taxpayer as does not exceed the zero bracket threshold, (B) 2 percent of so much of the net value of all taxable assets of the taxpayer in excess of the zero bracket threshold but not in excess of the top bracket threshold, plus (C) the applicable percentage of so much of the net value of all such taxable assets of the taxpayer in excess of the top bracket threshold. (2) Zero bracket threshold; top bracket threshold For purposes of this section\u2014 (A) Zero bracket threshold The zero bracket threshold is $50,000,000. (B) Top bracket threshold The top bracket threshold is $1,000,000,000. (c) Applicable percentage (1) In general For purposes of this section, the applicable percentage is\u2014 (A) except as provided in subparagraph (B), 3 percent, and (B) in the case of any calendar year in which there is in effect legislation which meets the requirements of paragraph (2), 6 percent. (2) Legislation described Legislation meets the requirements of this paragraph if such legislation\u2014 (A) establishes a health insurance program that provides to all residents of the United States comprehensive protection against the costs of health care and health-related services, and (B) prohibits private entities from providing duplicate benefits. (d) Treatment of married individuals For purposes of this section, individuals who are married (as defined in section 7703) shall be treated as one taxpayer. (e) Treatment of nongrantor multibeneficiary trusts (1) In general Any trust or portion of a trust which is a nongrantor multibeneficiary trust shall be treated as an individual to whom this chapter applies. (2) Computation of tax (A) In general In applying this chapter to a nongrantor multibeneficiary trust\u2014 (i) the zero bracket threshold shall be equal to the sum of\u2014 (I) $0, plus (II) the lowest unused 0 percent bracket amount assigned to the trust by all beneficiaries of the trust, and (ii) the top bracket threshold shall be equal to the sum of\u2014 (I) $0, plus (II) the lowest unused 2 percent bracket amount assigned to the trust by all beneficiaries of the trust. (B) Unused 0 percent bracket amount For purposes of this paragraph, the term unused 0 percent bracket amount means, with respect to any beneficiary for any calendar year, the lesser of\u2014 (i) the excess (if any) of\u2014 (I) the zero bracket threshold, over (II) the sum of\u2014 (aa) the net value of all taxable assets of the beneficiary for the calendar year, plus (bb) any unused 0 percent bracket amount assigned by the beneficiary to other nongrantor multibeneficiary trusts, or (ii) the portion of the net value of all taxable assets of the trust which such beneficiary is eligible to receive. (C) Unused 2 percent bracket amount For purposes of this paragraph, the term unused 2 percent bracket amount means, with respect to any beneficiary for any calendar year, the lesser of\u2014 (i) the excess (if any) of\u2014 (I) the top bracket threshold reduced by the zero bracket threshold, over (II) the sum of\u2014 (aa) the net value of all taxable assets of the beneficiary for the calendar year in excess of the zero bracket threshold, plus (bb) any unused 2 percent bracket amount assigned by the beneficiary to other nongrantor multibeneficiary trusts, or (ii) the portion of the net value of all taxable assets of the trust which such beneficiary is eligible to receive. (D) Assignment of amounts The assignment of any amount of unused 0 percent bracket amount and unused 2 percent bracket amount shall be made at such time and in such manner as specified by the Secretary in regulations. In any case in which no affirmative assignment is made by a beneficiary, the amount assigned shall be $0. (3) Nongrantor multibeneficiary trust For purposes of this chapter\u2014 (A) In general The term nongrantor multibeneficiary trust means any trust or portion of a trust\u2014 (i) with respect to which no person is treated as an owner under subpart E of subchapter J of chapter 1, (ii) no property of which is attributable to a gratuitous transfer of assets by a person who is subject to tax under this chapter for the calendar year, and (iii) which has more than one beneficiary (determined as of the last day of the calendar year). (B) Exception Such term shall not include\u2014 (i) any trust described in section 401(a) and exempt from tax under section 501(a), (ii) any trust all of the unexpired interests in which are devoted to one or more of the purposes described in section 170(c)(2)(B), (iii) any charitable lead annuity trust (as defined in section 2642(e)(3)) or charitable lead unitrust, or (iv) any charitable annuity remainder trust (as defined in section 664(d)(1)) or any charitable remainder unitrust (as defined in section 664(d)(2)). (C) Beneficiary The term beneficiary shall not include any person whose interest in a trust is contingent on the death of another person with an interest in such trust. 2902. Net value of taxable assets (a) In general For purposes of this subtitle, the term net value of all taxable assets means, as of any date, the value of all property of the taxpayer (other than property excluded under subsection (b)), real or personal, tangible or intangible, wherever situated, reduced by any debts (including any debts secured by property excluded under subsection (b)) owed by the taxpayer. (b) Exclusion for certain assets Property of the taxpayer shall not be taken into account under subsection (a) if such property\u2014 (1) has a value of $50,000 or less (determined without regard to any debt owed by the taxpayer with respect to such property), (2) is tangible personal property, and (3) is not property\u2014 (A) which is used in a trade or business of the taxpayer, (B) in connection with which a deduction is allowable under section 212, or (C) which is a collectible as defined in section 408(m), a boat, an aircraft, a mobile home, a trailer, a vehicle, or an antique or other asset that maintains or increases its value over time (within the meaning of section 5.02(2) of Revenue Procedure 2018\u201308). (c) Rules for determining property of the taxpayer For purposes of this subtitle\u2014 (1) Property included in estate Any property that would be included in the estate of the taxpayer if the taxpayer died shall be treated as property of the taxpayer. (2) Inclusion of certain gifts Any property transferred by the taxpayer after the date of the enactment of this chapter, to an individual who is a member of the family of the taxpayer (as determined under section 267(c)(4)) and has not attained the age of 18 shall be treated as property of the taxpayer for any calendar year before the year in which such individual attains the age of 18. (3) Attribution of property held by trusts (A) Grantor trusts If an individual is treated as the owner of any portion of a trust under subpart E of subchapter J of chapter 1, property attributable to such trust or portion of the trust shall be treated as property of the individual and not as property of the trust. (B) Nongrantor trusts (i) In general In the case of a trust or portion of a trust which is not described in subparagraph (A), any property which is attributable to a gratuitous transfer of assets by an individual who is subject to tax under this chapter for the calendar year shall be treated as property of such individual and not as property of the trust. (ii) Other trusts (I) In general In the case of any trust or portion of a trust which is described in subclause (II), the property of such trust shall be treated as the property of the beneficiary of such trust and not as the property of the trust. (II) Trusts to which this subclause applies A trust is described in this subclause if such trust not described in subparagraph (A), the assets of such trust are not attributable to a gratuitous transfer of assets by a person who is subject to tax under this chapter for the calendar year, and such trust has a single beneficiary (determined as of the last day of the calendar year). (C) Right of recovery (i) In general If any part of the net value of taxable assets of an individual on which tax has been paid consists of the value of property held by a trust which is included in the net value of taxable assets of such individual by reason of subparagraph (B), then such individual shall be entitled to recover from the trust the amount which bears the same ratio to the recoverable amount as\u2014 (I) the value of such property, bears to (II) the net value of taxable assets of the taxpayer. (ii) Recoverable amount For purposes of clause (i), the recoverable amount with respect to any trust is the excess of\u2014 (I) the tax imposed under this chapter for the calendar year on the individual, over (II) the amount of such tax which would be imposed for such calendar year on such individual if no property held by such trust were included in the net value of taxable assets of the individual. (iii) Treatment where no recovery In any case where a trust does not reimburse any taxpayer as provided in clause (i), the taxpayer shall be treated for purposes of this chapter as having made a gratuitous transfer to the trust in an amount equal to the amount determined under clause (i). Such transfer shall be treated as having been made on the last day of the calendar year for which the tax under subsection (a) was due. (4) Treatment of assets held by certain split-interest trusts (A) Remainder interests in charitable remainder annuity trusts and charitable remainder unitrusts In the case of any charitable remainder annuity trust (as defined in section 664(d)(1)) or of a charitable remainder unitrust (as defined in section 664(d)(2))\u2014 (i) the present value of any remainder interest shall not be taken into account under subsection (a), and (ii) the present value of any other interests shall be taken in account under subsection (a), in accordance with regulations promulgated by the Secretary, as the property of the beneficiaries of such interests. (B) Charitable lead annuity trusts and charitable lead unitrusts In the case of a charitable lead annuity trust (as defined in section 2642(e)(3)) or a charitable lead unitrust\u2014 (i) the present value of any interest described in section 2522(c)(2)(B) shall not be taken into account under subsection (a), and (ii) notwithstanding paragraphs (A) and (B) of paragraph (3), the present value of any remainder interest shall be taken into account under subsection (a), in accordance with regulations promulgated by the Secretary, as the property of the beneficiaries of such remainder interest. (d) Establishment of valuation rules Not later than 12 months after the date of the enactment of this section, the Secretary shall establish rules and methods for determining the value of any asset for purposes of this subtitle, including rules for the valuation of assets that are not publicly traded or that do not have a readily ascertainable value. Such rules and methods\u2014 (1) may utilize retrospective and prospective formulaic valuation methods not currently in use by the Secretary, (2) may require the use of formulaic valuation approaches for designated assets, including formulaic approaches based on proxies for determining presumptive valuations, formulaic approaches based on prospective adjustments from purchase prices or other prior events, or formulaic approaches based on retrospectively adding deferral charges based on eventual sale prices or other specified later events indicative of valuation, and (3) may address the use of valuation discounts. 2903. Special rules (a) Deceased individuals (1) In general In the case of any individual who dies during a calendar year and who is not married on the date of such individual's death\u2014 (A) section 2901(a) shall be applied by substituting the date of the individual's death for the last day of the calendar year , and (B) the amount of the tax imposed under such section shall be reduced by an amount which bears the same ratio to such amount (determined without regard to this subsection) as\u2014 (i) the number of days in the calendar year after the date of the individual's death, bears to (ii) 365. (2) Coordination with estate tax For purposes of section 2053, the tax imposed by this section for the year of the decedent's death shall be considered to have been imposed before such death. (b) Application to non-Residents In the case of any individual who is a non-resident and not a citizen of the United States, this subtitle shall apply only to the property of such individual which is situated in the United States (determined under rules similar to the rules under subchapter B of chapter 11). (c) Application to covered expatriates In the case of an individual who is a covered expatriate (as defined in section 877A), section 2901(a) shall be applied\u2014 (1) as if the calendar year ended on the day before the expatriation, and (2) as if the rate of tax under both subparagraphs (A) and (B) of section 2901(b)(1) were 40 percent. 2904. Information reporting (a) In general Not later than 12 months after the date of the enactment of this section, the Secretary shall by regulations require the reporting of any information concerning the net value of assets appropriate to enforce the tax imposed by this chapter. (b) Method of reporting The Secretary shall, where appropriate, require the reporting made under subsection (a) to be made as a part of existing income reporting requirements (including requirements under chapter 4 (relating to taxes to enforce reporting on certain foreign accounts)). (c) Responsibility for reporting The Secretary may impose reporting obligations by reference to the ownership, control, management, claim to income from, or other relationship to assets and liabilities for purposes of administering the tax imposed by this section and may impose such obligations on financial institutions, business entities, or other persons, including requiring business entities to provide estimates of the value of the entity itself. 2905. Enforcement The Secretary shall annually audit not less than 30 percent of taxpayers required to pay the tax imposed under this chapter. .\n##### (b) No deduction from income taxes\nSection 275 of the Internal Revenue Code of 1986 is amended by inserting after paragraph (6) the following new paragraph:\n(7) Taxes imposed by chapter 18. .\n##### (c) Extension of time for payment of tax\n**(1) In general**\nSection 6161(a) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Wealth tax (A) In general In the case of taxpayer described in subparagraph (B), the Secretary may extend the time for payment of the tax imposed under chapter 18 for a reasonable period not to exceed 5 years from the date fixed for the payment thereof. (B) Taxpayers described A taxpayer is described in this subparagraph if such the Secretary determines\u2014 (i) the taxpayer has severe liquidity constraints, or (ii) immediate payment would cause undue hardship on an ongoing enterprise. .\n**(2) Rules**\nNot later than 12 months after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary's delegate) shall establish rules for the application of the amendments made by paragraph (1).\n##### (d) Application of accuracy related penalties\n**(1) In general**\nSection 6662(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(11) Any substantial wealth tax valuation understatement. .\n**(2) Substantial wealth tax understatement**\nSection 6662 of such Code is amended by adding at the end the following new subsection:\n(n) Application to substantial wealth tax valuation understatement (1) Substantial wealth tax valuation understatement defined (A) In general For purposes of this section, there is a substantial wealth tax valuation understatement if the value of any property claimed on any return of tax imposed by subtitle B\u20131 is 65 percent or less of the amount determined to be the correct amount of such valuation. (B) Limitation No penalty shall be imposed by reason of subsection (b)(11) unless the portion of the underpayment attributable to substantial wealth tax valuation understatements for the calendar year exceeds $5,000. (2) Increased penalty (A) In general In the case of any portion of an underpayment which is attributable to one or more substantial wealth tax valuation understatement, subsection (a) shall be applied\u2014 (i) in the case of a substantial wealth tax valuation understatement which is a gross wealth tax valuation misstatement, by substituting 50 percent for 20 percent , and (ii) in any other case, by substituting 30 percent for 20 percent . (B) Gross wealth tax valuation misstatement For purposes of subparagraph (A), the term gross wealth tax valuation misstatement means a substantial wealth tax valuation understatement, as determined under paragraph (1) by substituting 40 percent for 65 percent . .\n##### (e) Clerical amendment\nThe table of subtitles of such Code is amended by inserting after the item relating to subtitle B the following new item:\nSubtitle B\u20131\u2014Wealth tax .\n##### (f) Effective date\nThe amendments made by this section shall apply to calendar years beginning after December 31, 2026.\n##### (g) Periodic reports\nNot later than January 1, 2029, and every 2 years thereafter, the Secretary of the Treasury (or the Secretary's delegate) shall submit to Congress a report on the tax imposed under chapter 18 of the Internal Revenue Code of 1986 (as added by this Act), including any issues related to the administration and enforcement of such tax.\n#### 3. Strengthening disclosure requirements\n##### (a) Regulatory authority\nThe Secretary of the Treasury (or the Secretary's delegate) may issue such rules and regulations as necessary to prevent taxpayers from avoiding the purpose of information reporting requirements under the Internal Revenue Code of 1986 by placing assets in any foreign corporation, partnership, or trust in which the taxpayer holds directly or indirectly, a significant interest as the sole or principal owner or the sole or principal beneficial owner.\n##### (b) FATCA enforcement plan\nThe Secretary of the Treasury (or the Secretary's delegate) shall develop a comprehensive plan for managing efforts to leverage data collected under chapter 4 of the Internal Revenue Code of 1986 in agency compliance efforts. Such plan shall include an evaluation of the extent to which actions being undertaken as of the date of the enactment of this Act for the enforcement of the requirements of such chapter improve voluntary compliance and address noncompliance with such requirements.\n#### 4. Internal Revenue Service funding\n##### (a) In general\nSubchapter A of chapter 80 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n7813. Authorization of appropriations There are authorized to be appropriated to the Secretary for the period of fiscal years 2027 through 2037\u2014 (1) for enforcement of this title, $70,000,000,000, (2) for taxpayer services, $10,000,000,000, and (3) for business system modernization, $20,000,000,000. .\n##### (b) Clerical amendment\nThe table of sections for subchapter A of chapter 80 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 7813. Authorization of appropriations. .",
      "versionDate": "2026-03-25",
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
        "actionDate": "2026-03-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4246",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ultra-Millionaire Tax Act of 2026",
      "type": "S"
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
        "updateDate": "2026-03-31T21:36:32Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8085ih.xml"
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
      "title": "Ultra-Millionaire Tax Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-26T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Ultra-Millionaire Tax Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-26T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to impose a tax on the net value of assets of a taxpayer, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T08:18:31Z"
    }
  ]
}
```
