# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8080?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8080
- Title: Data to Save Moms Act
- Congress: 119
- Bill type: HR
- Bill number: 8080
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-05-13T08:06:08Z
- Update date including text: 2026-05-13T08:06:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-25 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-25 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8080",
    "number": "8080",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000629",
        "district": "3",
        "firstName": "Sharice",
        "fullName": "Rep. Davids, Sharice [D-KS-3]",
        "lastName": "Davids",
        "party": "D",
        "state": "KS"
      }
    ],
    "title": "Data to Save Moms Act",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:08Z",
    "updateDateIncludingText": "2026-05-13T08:06:08Z"
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
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2026-03-25T14:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-25T14:01:00Z",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "M001245",
      "district": "18",
      "firstName": "Christian",
      "fullName": "Rep. Menefee, Christian D. [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Menefee",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MO"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "TN"
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
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MI"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NV"
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "OH"
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "AL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
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
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NJ"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "KY"
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IN"
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "TX"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "WI"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8080ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8080\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Ms. Davids of Kansas (for herself, Mrs. McIver , Ms. Tlaib , Ms. Norton , Mrs. Watson Coleman , Ms. Kamlager-Dove , Mr. Johnson of Georgia , Ms. Pressley , Mr. Ivey , Mr. Krishnamoorthi , Mrs. Cherfilus-McCormick , Mr. Menefee , Mr. Bell , Mr. Moulton , Ms. Clarke of New York , Ms. DelBene , Mr. Garamendi , Mr. Cohen , Ms. Stansbury , Mrs. Dingell , Ms. Jacobs , Mr. Figures , Mr. Horsford , Mr. Garc\u00eda of Illinois , Mr. Veasey , Mrs. Beatty , Mr. Smith of Washington , Ms. Sewell , Ms. Wilson of Florida , Mr. Jackson of Illinois , Mr. Conaway , Mr. Scott of Virginia , Mrs. Hayes , Ms. Craig , Mr. McGarvey , Mrs. Grijalva , Mr. Carson , Mr. Takano , Mrs. McBath , Mr. Latimer , Ms. Johnson of Texas , Mr. Soto , Ms. Underwood , and Ms. Moore of Wisconsin ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Public Health Service Act to improve maternal health data collection processes and quality measures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Data to Save Moms Act .\n#### 2. Funding for maternal mortality review committees to promote representative community engagement\n##### (a) In general\nSection 317K(d) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(d) ) is amended by adding at the end the following:\n(9) Grants to promote representative community engagement in maternal mortality review committees (A) In general The Secretary may, using funds made available pursuant to subparagraph (C), provide assistance to an applicable maternal mortality review committee of a State, Indian Tribe, Tribal organization, or Urban Indian organization (as such terms are defined in section 4 of the Indian Health Care Improvement Act)\u2014 (i) to select for inclusion in the membership of such a committee community members from the State, Indian Tribe, Tribal organization, or Urban Indian organization by\u2014 (I) prioritizing community members who can increase the diversity of the committee\u2019s membership with respect to race and ethnicity, location, personal or family experiences of maternal mortality or severe maternal morbidity, and professional background, including members with nonclinical experiences; and (II) to the extent applicable, using funds reserved under subsection (f), to address barriers to maternal mortality review committee participation for community members, including required training, transportation barriers, compensation, and other supports as may be necessary; (ii) to establish initiatives to conduct outreach and community engagement efforts within communities throughout the State or Tribe to seek input from community members on the work of such maternal mortality review committee, with a particular focus on outreach to women from racial and ethnic minority groups (as such term is defined in section 1707(g)(1)); and (iii) to release public reports assessing\u2014 (I) the pregnancy-related death and pregnancy-associated death review processes of the maternal mortality review committee, with a particular focus on the maternal mortality review committee\u2019s sensitivity to the unique circumstances of pregnant and postpartum individuals from racial and ethnic minority groups (as such term is defined in section 1707(g)(1)) who have suffered pregnancy-related deaths; and (II) the impact of the use of funds made available pursuant to subparagraph (C) on increasing the diversity of the maternal mortality review committee membership and promoting community engagement efforts throughout the State or Tribe. (B) Technical assistance The Secretary shall provide (either directly through the Department of Health and Human Services or by contract) technical assistance to any maternal mortality review committee receiving a grant under this paragraph on best practices for increasing the diversity of the maternal mortality review committee\u2019s membership and for conducting effective community engagement throughout the State or Tribe. (C) Authorization of appropriations In addition to any funds made available under subsection (f), there is authorized to be appropriated to carry out this paragraph $10,000,000 for each of fiscal years 2027 through 2031. .\n##### (b) Reservation of funds\nSection 317K(f) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(f) ) is amended by adding at the end the following: Of the amount made available under the preceding sentence for a fiscal year, not less than $1,500,000 shall be reserved for grants to Indian Tribes, Tribal organizations, or Urban Indian organizations (as those terms are defined in section 4 of the Indian Health Care Improvement Act) .\n#### 3. Data collection and review\nSection 317K(d)(3)(A)(i) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(d)(3)(A)(i) ) is amended\u2014\n**(1)**\nby redesignating subclauses (II) and (III) as subclauses (V) and (VI), respectively; and\n**(2)**\nby inserting after subclause (I) the following:\n(II) to the extent practicable, reviewing cases of severe maternal morbidity, according to the most up-to-date indicators; (III) to the extent practicable, reviewing deaths during pregnancy or up to 1 year after the end of a pregnancy from suicide, overdose, or other death from a mental health condition or substance use disorder attributed to or aggravated by pregnancy or childbirth complications; (IV) to the extent practicable, consulting with local community-based organizations representing pregnant and postpartum individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes to ensure that, in addition to clinical factors, nonclinical factors that might have contributed to a pregnancy-related death are appropriately considered; .\n#### 4. Review of maternal health data collection processes and quality measures\n##### (a) In general\nThe Secretary of Health and Human Services, acting through the Administrator of the Centers for Medicare & Medicaid Services and the Director of the Agency for Healthcare Research and Quality, shall consult with relevant stakeholders\u2014\n**(1)**\nto review existing maternal health data collection processes and quality measures; and\n**(2)**\nto make recommendations to improve such processes and measures, including topics described under subsection (c).\n##### (b) Collaboration\nIn carrying out this section, the Secretary shall consult with a diverse group of maternal health stakeholders, which may include\u2014\n**(1)**\npregnant and postpartum individuals and their family members, and nonprofit organizations representing such individuals, with a particular focus on patients from racial and ethnic minority groups;\n**(2)**\ncommunity-based organizations that provide support for pregnant and postpartum individuals, with a particular focus on patients from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(3)**\nmembership organizations for maternity care providers;\n**(4)**\norganizations representing perinatal health workers;\n**(5)**\norganizations that focus on maternal mental or behavioral health;\n**(6)**\norganizations that focus on intimate partner violence;\n**(7)**\ninstitutions of higher education, with a particular focus on minority-serving institutions;\n**(8)**\nlicensed and accredited hospitals, birth centers, midwifery practices, or other facilities that provide maternal health care services;\n**(9)**\nrelevant State and local public agencies, including State maternal mortality review committees; and\n**(10)**\nthe National Quality Forum, or such other standard-setting organizations specified by the Secretary.\n##### (c) Topics\nThe review of maternal health data collection processes and recommendations to improve such processes and measures required under subsection (a) shall assess all available relevant information, including information from State-level sources, and shall consider at least the following:\n**(1)**\nCurrent State and Tribal practices for maternal health, maternal mortality, and severe maternal morbidity data collection and dissemination, including consideration of\u2014\n**(A)**\nthe timeliness of processes for amending a death certificate when new information pertaining to the death becomes available to reflect whether the death was a pregnancy-related death;\n**(B)**\nrelevant data collected with electronic health records, including data on race, ethnicity, primary language, socioeconomic status, geography, insurance type, and other relevant demographic information;\n**(C)**\nmaternal health data collected and publicly reported by hospitals, health systems, midwifery practices, and birth centers;\n**(D)**\nthe barriers preventing States from correlating maternal outcome data with data on race, ethnicity, and other demographic characteristics;\n**(E)**\nprocesses for determining the cause of a pregnancy-associated death in States that do not have a maternal mortality review committee;\n**(F)**\nwhether maternal mortality review committees include multidisciplinary and diverse membership (as described in section 317K(d)(1)(A) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(d)(1)(A) ));\n**(G)**\nwhether members of maternal mortality review committees participate in trainings on bias, racism, or discrimination, and the quality of such trainings;\n**(H)**\nthe extent to which States have implemented systematic processes of listening to the stories of pregnant and postpartum individuals and their family members, with a particular focus on pregnant and postpartum individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes, and their family members, to fully understand the causes of, and inform potential solutions to, the maternal mortality and severe maternal morbidity crisis within their respective States;\n**(I)**\nthe extent to which maternal mortality review committees are considering social determinants of maternal health when examining the causes of pregnancy-associated and pregnancy-related deaths;\n**(J)**\nthe extent to which maternal mortality review committees are making actionable recommendations based on their reviews of adverse maternal health outcomes and the extent to which such recommendations are being implemented by appropriate stakeholders;\n**(K)**\nthe legal and administrative barriers preventing the collection, collation, and dissemination of State maternity care data;\n**(L)**\nthe effectiveness of data collection and reporting processes in separating pregnancy-associated deaths from pregnancy-related deaths; and\n**(M)**\nthe current Federal, State, local, and Tribal funding support for the activities referred to in subparagraphs (A) through (L).\n**(2)**\nWhether the funding support referred to in paragraph (1)(M) is adequate for States to carry out optimal data collection and dissemination processes with respect to maternal health, maternal mortality, and severe maternal morbidity.\n**(3)**\nCurrent quality measures for maternity care, including prenatal measures, labor and delivery measures, and postpartum measures, including topics such as\u2014\n**(A)**\neffective quality measures for maternity care used by hospitals, health systems, midwifery practices, birth centers, health plans, and other relevant entities;\n**(B)**\nthe sufficiency of current outcome measures used to evaluate maternity care for driving improved care, experiences, and outcomes in maternity care payment and delivery system models;\n**(C)**\nmaternal health quality measures that other countries effectively use;\n**(D)**\nvalidated measures that have been used for research purposes that could be tested, refined, and submitted for national endorsement;\n**(E)**\nbarriers preventing maternity care providers and insurers from implementing quality measures that are aligned with best practices;\n**(F)**\nthe frequency with which maternity care quality measures are reviewed and revised;\n**(G)**\nthe strengths and weaknesses of the Prenatal and Postpartum Care measures of the Health Plan Employer Data and Information Set measures established by the National Committee for Quality Assurance;\n**(H)**\nthe strengths and weaknesses of maternity care quality measures under the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) and the Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397 et seq. ), including the extent to which States voluntarily report relevant measures;\n**(I)**\nthe extent to which maternity care quality measures are informed by patient experiences that include measures of patient-reported experience of care;\n**(J)**\nthe current processes for collecting and making publicly available, to the extent practicable, stratified data on race, ethnicity, and other demographic characteristics of pregnant and postpartum individuals in hospitals, health systems, midwifery practices, and birth centers, and for incorporating such demographically stratified data in maternity care quality measures;\n**(K)**\nthe extent to which maternity care quality measures account for the unique experiences of pregnant and postpartum individuals from racial and ethnic minority groups; and\n**(L)**\nthe extent to which hospitals, health systems, midwifery practices, and birth centers are implementing existing maternity care quality measures.\n**(4)**\nRecommendations on authorizing additional funds and providing additional technical assistance to improve maternal mortality review committees and State and Tribal maternal health data collection and reporting processes.\n**(5)**\nRecommendations for new authorities that may be granted to maternal mortality review committees to be able to\u2014\n**(A)**\naccess records from other Federal and State agencies and departments that may be necessary to identify causes of pregnancy-associated and pregnancy-related deaths that are unique to pregnant and postpartum individuals from specific populations, such as veterans and individuals who are incarcerated; and\n**(B)**\nwork with relevant experts who are not members of the maternal mortality review committee to assist in the review of pregnancy-associated deaths of pregnant and postpartum individuals from specific populations, such as veterans and individuals who are incarcerated.\n**(6)**\nRecommendations to improve and standardize current quality measures for maternity care, with a particular focus on maternal health disparities.\n**(7)**\nRecommendations to improve the coordination by the Department of Health and Human Services of the efforts undertaken by the agencies and organizations within the Department related to maternal health data and quality measures.\n##### (d) Report\nNot later than 1 year after the enactment of this Act, the Secretary shall submit to the Congress and make publicly available a report on the results of the review of maternal health data collection processes and quality measures and recommendations to improve such processes and measures required under subsection (a).\n##### (e) Definition\nIn this section, the term maternal mortality review committee means a maternal mortality review committee duly authorized by a State and receiving funding under section 317K(a)(2)(D) of the Public Health Service Act ( 42 U.S.C. 247b\u201312(a)(2)(D) ).\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this section for fiscal years 2027 through 2030.\n#### 5. Study on maternal health among American Indian and Alaska Native individuals\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall, in coordination with entities described in subsection (b)\u2014\n**(1)**\nnot later than 90 days after the enactment of this Act, enter into a contract with an independent research organization or Tribal Epidemiology Center to conduct a comprehensive study on maternal mortality, severe maternal morbidity, and other adverse perinatal or childbirth outcomes in the populations of American Indian and Alaska Native individuals; and\n**(2)**\nnot later than 3 years after the date of the enactment of this Act, submit to Congress a report on such study that contains recommendations for policies and practices that can be adopted to improve maternal health outcomes for American Indian and Alaska Native individuals.\n##### (b) Participating entities\nThe entities described in this subsection shall consist of 12 members, selected by the Secretary from among individuals nominated by Indian Tribes and Tribal organizations (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )), and Urban Indian organizations (as such term is defined in section 4 of the Indian Health Care Improvement Act ( 25 U.S.C. 1603 )). In selecting such members, the Secretary shall ensure that each of the 12 service areas of the Indian Health Service is represented.\n##### (c) Contents of study\nThe study conducted pursuant to subsection (a) shall\u2014\n**(1)**\nexamine the causes of maternal mortality and severe maternal morbidity that are unique to American Indian and Alaska Native individuals;\n**(2)**\ninclude a systematic process of listening to the stories of American Indian and Alaska Native individuals to fully understand the causes of, and inform potential solutions to, the maternal health crisis within their respective communities;\n**(3)**\ndistinguish between the causes of, landscape of maternity care at, and recommendations to improve maternal health outcomes within, the different settings in which American Indian and Alaska Native individuals receive maternity care, such as\u2014\n**(A)**\nfacilities operated by the Indian Health Service;\n**(B)**\nan Indian health program operated by an Indian Tribe or Tribal organization pursuant to a contract, grant, cooperative agreement, or compact with the Indian Health Service pursuant to the Indian Self-Determination Act;\n**(C)**\nan urban Indian health program operated by an Urban Indian organization pursuant to a grant or contract with the Indian Health Service pursuant to title V of the Indian Health Care Improvement Act; and\n**(D)**\nfacilities outside of the Indian Health Service in which American Indian and Alaska Native individuals receive maternity care services;\n**(4)**\nreview processes for coordinating programs of the Indian Health Service with social services provided through other programs administered by the Secretary of Health and Human Services (other than the Medicare Program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), the Medicaid Program under title XIX of such Act ( 42 U.S.C. 1396 et seq. ), and the Children\u2019s Health Insurance Program under title XXI of such Act ( 42 U.S.C. 1397 et seq. ));\n**(5)**\nreview current data collection and quality measurement processes and practices;\n**(6)**\nassess causes and frequency of maternal mental health conditions and substance use disorders;\n**(7)**\nconsider social determinants of health, including poverty, lack of health insurance, unemployment, sexual and domestic violence, and environmental conditions in Tribal areas;\n**(8)**\nconsider the role that historical mistreatment of American Indian and Alaska Native women has played in causing currently elevated rates of maternal mortality, severe maternal morbidity, and other adverse perinatal or childbirth outcomes;\n**(9)**\nconsider how current funding of the Indian Health Service affects the ability of the Service to deliver quality maternity care;\n**(10)**\nconsider the extent to which the delivery of maternity care services is culturally appropriate for American Indian and Alaska Native individuals;\n**(11)**\nmake recommendations to reduce misclassification of American Indian and Alaska Native individuals, including consideration of best practices in training for maternal mortality review committee members to be able to correctly classify American Indian and Alaska Native individuals; and\n**(12)**\nmake recommendations informed by the stories shared by American Indian and Alaska Native individuals referred to in paragraph (2) to improve maternal health outcomes for such individuals.\n##### (d) Report\nThe agreement entered into under subsection (a) with an independent research organization or Tribal Epidemiology Center shall require that the organization or Center transmit to Congress a report on the results of the study conducted pursuant to that agreement not later than 36 months after the date of the enactment of this Act.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $2,000,000 for each of fiscal years 2027 through 2029.\n#### 6. Grants to minority-serving institutions to study maternal mortality, severe maternal morbidity, and other adverse maternal health outcomes\n##### (a) In general\nThe Secretary of Health and Human Services shall establish a program under which the Secretary shall award grants to research centers, health professions schools and programs, and other entities at minority-serving institutions to study specific aspects of the maternal health crisis among pregnant and postpartum individuals from racial and ethnic minority groups. Such research may\u2014\n**(1)**\ninclude the development and implementation of systematic processes of listening to the stories of pregnant and postpartum individuals from racial and ethnic minority groups, and perinatal health workers supporting such individuals, to fully understand the causes of, and inform potential solutions to, the maternal mortality and severe maternal morbidity crisis within their respective communities;\n**(2)**\nassess the potential causes of relatively low rates of maternal mortality among Hispanic individuals, including potential racial misclassification and other data collection and reporting issues that might be misrepresenting maternal mortality rates among Hispanic individuals in the United States;\n**(3)**\nassess differences in rates of adverse maternal health outcomes among subgroups identifying as Hispanic, including disparities in access to early prenatal care; and\n**(4)**\ninclude lactation education to promote racial and ethnic diversity within the workforce of health care professionals with breastfeeding and lactation expertise.\n##### (b) Application\nTo be eligible to receive a grant under subsection (a), an entity described in such subsection shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require.\n##### (c) Technical assistance\nThe Secretary may use not more than 10 percent of the funds made available under subsection (g)\u2014\n**(1)**\nto conduct outreach to minority-serving institutions to raise awareness of the availability of grants under subsection (a);\n**(2)**\nto provide technical assistance in the application process for such a grant; and\n**(3)**\nto promote capacity building as needed to enable entities described in such subsection to submit such an application.\n##### (d) Reporting requirement\nEach entity awarded a grant under this section shall periodically submit to the Secretary a report on the status of activities conducted using the grant.\n##### (e) Evaluation\nBeginning 1 year after the date on which the first grant is awarded under this section, the Secretary shall submit to Congress an annual report summarizing the findings of research conducted using funds made available under this section.\n##### (f) Minority-Serving institutions defined\nIn this section, the term minority-serving institution has the meaning given the term in section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) ).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2027 through 2031.\n#### 7. Definitions\nIn this Act:\n**(1) Maternity care provider**\nThe term maternity care provider means a health care provider who\u2014\n**(A)**\nis a physician, a physician assistant, a midwife who meets, at a minimum, the international definition of a midwife and global standards for midwifery education as established by the International Confederation of Midwives, an advanced practice registered nurse, a doula accredited by a State to receive reimbursement for doula services under a State plan (or a waiver of such plan) under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), or a lactation consultant certified by the International Board of Lactation Consultant Examiners; and\n**(B)**\nhas a focus on maternal or perinatal health.\n**(2) Perinatal health worker**\nThe term perinatal health worker means a nonclinical health worker focused on maternal or perinatal health, such as a doula, community health worker, peer supporter, lactation educator or counselor, nutritionist or dietitian, childbirth educator, social worker, home visitor, patient navigator or coordinator, or language interpreter.\n**(3) Postpartum**\nThe term postpartum refers to the 1-year period beginning on the last day of the pregnancy of an individual.\n**(4) Pregnancy-associated death**\nThe term pregnancy-associated death means a death of a pregnant or postpartum individual, by any cause, that occurs during, or within 1 year following, the individual\u2019s pregnancy, regardless of the outcome, duration, or site of the pregnancy.\n**(5) Pregnancy-related death**\nThe term pregnancy-related death means a death of a pregnant or postpartum individual that occurs during, or within 1 year following, the individual\u2019s pregnancy, from a pregnancy complication, a chain of events initiated by pregnancy, or the aggravation of an unrelated condition by the physiologic effects of pregnancy.\n**(6) Racial and ethnic minority group**\nThe term racial and ethnic minority group has the meaning given such term in section 1707(g)(1) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g)(1) ).\n**(7) Severe maternal morbidity**\nThe term severe maternal morbidity means a health condition, including mental health conditions and substance use disorders, attributed to or aggravated by pregnancy or childbirth that results in significant short-term or long-term consequences to the health of the individual who was pregnant.\n**(8) Social determinants of maternal health**\nThe term social determinants of maternal health means nonclinical factors that impact maternal health outcomes.",
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
        "actionDate": "2026-03-25",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4187",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Data to Save Moms Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, Veterans' Affairs, Natural Resources, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7973",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Momnibus Act",
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
        "name": "Health",
        "updateDate": "2026-04-13T13:53:17Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8080ih.xml"
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
      "title": "Data to Save Moms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Data to Save Moms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to improve maternal health data collection processes and quality measures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:25Z"
    }
  ]
}
```
