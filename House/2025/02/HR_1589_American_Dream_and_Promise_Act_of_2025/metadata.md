# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1589?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1589
- Title: American Dream and Promise Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1589
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-11-21T12:03:59Z
- Update date including text: 2025-11-21T12:03:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H884)
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-26 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H884)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1589",
    "number": "1589",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000587",
        "district": "29",
        "firstName": "Sylvia",
        "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
        "lastName": "Garcia",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "American Dream and Promise Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-21T12:03:59Z",
    "updateDateIncludingText": "2025-11-21T12:03:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H884)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-26T15:03:00Z",
          "name": "Referred To"
        }
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "J000294",
      "district": "8",
      "firstName": "Hakeem",
      "fullName": "Rep. Jeffries, Hakeem S. [D-NY-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Jeffries",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001101",
      "district": "5",
      "firstName": "Katherine",
      "fullName": "Rep. Clark, Katherine M. [D-MA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Clark",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "A000371",
      "district": "33",
      "firstName": "Pete",
      "fullName": "Rep. Aguilar, Pete [D-CA-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Aguilar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CO"
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
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
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
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
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
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NM"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
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
      "sponsorshipDate": "2025-02-26",
      "state": "AZ"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000197",
      "district": "11",
      "firstName": "Nancy",
      "fullName": "Rep. Pelosi, Nancy [D-CA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pelosi",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz [D-CA-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray, Jr. [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CO"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CO"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CO"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CT"
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
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "DE"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "HI"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "KS"
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
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "IN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "KY"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "LA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MD"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "ME"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NC"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NM"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NM"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NV"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NV"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OR"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-26",
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
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jos\u00e9",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PR"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "RI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "RI"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "SC"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TN"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
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
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "P000610",
      "district": "0",
      "firstName": "Stacey",
      "fullName": "Del. Plaskett, Stacey E. [D-VI-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Plaskett",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VI"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VT"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "WI"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "CA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NH"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "CA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "OH"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "LA"
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
      "sponsorshipDate": "2025-06-11",
      "state": "MA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "HI"
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
      "sponsorshipDate": "2025-06-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "NV"
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
      "sponsorshipDate": "2025-07-21",
      "state": "OH"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "FL"
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
      "sponsorshipDate": "2025-11-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1589ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1589\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Ms. Garcia of Texas (for herself, Ms. Vel\u00e1zquez , Ms. Clarke of New York , Ms. Salazar , Ms. Lofgren , Ms. Jayapal , Mrs. Ramirez , Mr. Correa , Ms. Chu , Mr. Jeffries , Ms. Clark of Massachusetts , Mr. Aguilar , Mr. Lieu , Mr. Neguse , Ms. DelBene , Mr. Raskin , Ms. DeLauro , Mr. Thompson of Mississippi , Mr. Scott of Virginia , Ms. Waters , Mr. Pallone , Mr. Neal , Mr. Smith of Washington , Ms. Craig , Mr. Meeks , Mr. Takano , Mr. Larsen of Washington , Mr. Huffman , Mr. Himes , Mr. Morelle , Mr. McGovern , Mr. Connolly , Mr. Espaillat , Mr. Casar , Ms. Meng , Ms. Leger Fernandez , Mr. Figures , Ms. Sewell , Ms. Ansari , Mr. Stanton , Mr. Grijalva , Mr. Thompson of California , Mr. Bera , Ms. Matsui , Mr. Garamendi , Mr. Harder of California , Mr. DeSaulnier , Ms. Pelosi , Ms. Simon , Mr. Gray , Mr. Swalwell , Mr. Mullin , Mr. Liccardo , Mr. Khanna , Mr. Panetta , Mr. Costa , Mr. Carbajal , Ms. Brownley , Mr. Whitesides , Ms. Rivas , Mr. Cisneros , Mr. Ruiz , Ms. Friedman , Mr. Sherman , Mr. Gomez , Mrs. Torres of California , Ms. S\u00e1nchez , Mr. Garcia of California , Ms. Barrag\u00e1n , Mr. Tran , Mr. Levin , Mr. Peters , Ms. Jacobs , Mr. Vargas , Ms. DeGette , Mr. Crow , Ms. Pettersen , Mr. Larson of Connecticut , Mr. Courtney , Mrs. Hayes , Ms. Norton , Ms. McBride , Mr. Soto , Mr. Frost , Ms. Castor of Florida , Mrs. Cherfilus-McCormick , Ms. Wilson of Florida , Ms. Wasserman Schultz , Mr. Bishop , Mr. Johnson of Georgia , Ms. Williams of Georgia , Mrs. McBath , Mr. David Scott of Georgia , Ms. Tokuda , Ms. Davids of Kansas , Mr. Jackson of Illinois , Ms. Kelly of Illinois , Mr. Garc\u00eda of Illinois , Mr. Quigley , Mr. Casten , Mr. Davis of Illinois , Mr. Krishnamoorthi , Ms. Schakowsky , Mr. Schneider , Mr. Foster , Ms. Budzinski , Ms. Underwood , Mr. Sorensen , Mr. Mrvan , Mr. Carson , Mr. McGarvey , Mr. Carter of Louisiana , Mrs. Trahan , Mr. Moulton , Ms. Pressley , Mr. Keating , Mr. Olszewski , Ms. Elfreth , Mr. Ivey , Mr. Hoyer , Mrs. McClain Delaney , Mr. Mfume , Ms. Pingree , Ms. Scholten , Mrs. Dingell , Ms. McDonald Rivet , Ms. Stevens , Ms. Tlaib , Mr. Thanedar , Ms. Morrison , Ms. McCollum , Ms. Omar , Mr. Bell , Mr. Cleaver , Ms. Ross , Mrs. Foushee , Ms. Adams , Mr. Conaway , Mr. Gottheimer , Mr. Menendez , Ms. Pou , Mrs. McIver , Ms. Sherrill , Mrs. Watson Coleman , Ms. Stansbury , Mr. Vasquez , Ms. Titus , Mr. Horsford , Mr. Suozzi , Mr. Goldman of New York , Mr. Nadler , Ms. Ocasio-Cortez , Mr. Torres of New York , Mr. Latimer , Mr. Tonko , Mrs. Beatty , Ms. Brown , Ms. Bonamici , Ms. Dexter , Ms. Hoyle of Oregon , Ms. Bynum , Ms. Salinas , Mr. Boyle of Pennsylvania , Mr. Evans of Pennsylvania , Ms. Dean of Pennsylvania , Ms. Scanlon , Ms. Houlahan , Ms. Lee of Pennsylvania , Mr. Deluzio , Mr. Hern\u00e1ndez , Mr. Amo , Mr. Magaziner , Mr. Clyburn , Mr. Cohen , Mrs. Fletcher , Mr. Green of Texas , Ms. Escobar , Mr. Turner of Texas , Mr. Castro of Texas , Mr. Cuellar , Ms. Crockett , Ms. Johnson of Texas , Mr. Veasey , Mr. Doggett , Ms. McClellan , Mr. Vindman , Mr. Beyer , Mr. Subramanyam , Ms. Plaskett , Ms. Balint , Ms. Randall , Ms. Schrier , Ms. Strickland , Mr. Pocan , Ms. Moore of Wisconsin , Mr. Auchincloss , Mr. Min , Mr. Norcross , Ms. Lois Frankel of Florida , and Mr. Ryan ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the cancellation of removal and adjustment of status of certain aliens, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the American Dream and Promise Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTitle I\u2014Dream Act of 2025\nSec. 101. Short title.\nSec. 102. Permanent resident status on a conditional basis for certain long-term residents who entered the United States as children.\nSec. 103. Terms of permanent resident status on a conditional basis.\nSec. 104. Removal of conditional basis of permanent resident status.\nSec. 105. Restoration of State option to determine residency for purposes of higher education benefits.\nTitle II\u2014American Promise Act of 2025\nSec. 201. Short title.\nSec. 202. Adjustment of status for certain nationals of certain countries designated for temporary protected status or deferred enforced departure.\nSec. 203. Clarification.\nTitle III\u2014General Provisions\nSec. 301. Definitions.\nSec. 302. Submission of biometric and biographic data; background checks.\nSec. 303. Limitation on removal; application and fee exemption; and other conditions on eligible individuals.\nSec. 304. Determination of continuous presence and residence.\nSec. 305. Exemption from numerical limitations.\nSec. 306. Availability of administrative and judicial review.\nSec. 307. Documentation requirements.\nSec. 308. Rulemaking.\nSec. 309. Confidentiality of information.\nSec. 310. Grant program to assist eligible applicants.\nSec. 311. Provisions affecting eligibility for adjustment of status.\nSec. 312. Supplementary surcharge for appointed counsel.\nSec. 313. Annual report on provisional denial authority.\nI\nDream Act of 2025\n#### 101. Short title\nThis title may be cited as the Dream Act of 2025 .\n#### 102. Permanent resident status on a conditional basis for certain long-term residents who entered the United States as children\n##### (a) Conditional basis for status\nNotwithstanding any other provision of law, and except as provided in section 104(c)(2), an alien shall be considered, at the time of obtaining the status of an alien lawfully admitted for permanent residence under this section, to have obtained such status on a conditional basis subject to the provisions of this title.\n##### (b) Requirements\n**(1) In general**\nNotwithstanding any other provision of law, the Secretary or the Attorney General shall adjust to the status of an alien lawfully admitted for permanent residence on a conditional basis, or without the conditional basis as provided in section 104(c)(2), an alien who is inadmissible or deportable from the United States, is subject to a grant of Deferred Enforced Departure, has temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ), or is the son or daughter of an alien admitted as a nonimmigrant under subparagraph (E)(i), (E)(ii), (H)(i)(b), or (L) of section 101(a)(15) of such Act ( 8 U.S.C. 1101(a)(15) ) if\u2014\n**(A)**\nthe alien has been continuously physically present in the United States since January 1, 2021;\n**(B)**\nthe alien was 18 years of age or younger on the date on which the alien entered the United States and has continuously resided in the United States since such entry;\n**(C)**\nthe alien\u2014\n**(i)**\nsubject to paragraph (2), is not inadmissible under paragraph (1), (6)(E), (6)(G), (8), or (10) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) );\n**(ii)**\nhas not ordered, incited, assisted, or otherwise participated in the persecution of any person on account of race, religion, nationality, membership in a particular social group, or political opinion; and\n**(iii)**\nis not barred from adjustment of status under this title based on the criminal and national security grounds described under subsection (c), subject to the provisions of such subsection; and\n**(D)**\nthe alien\u2014\n**(i)**\nhas been admitted to an institution of higher education;\n**(ii)**\nhas been admitted to an area career and technical education school at the postsecondary level;\n**(iii)**\nin the United States, has obtained\u2014\n**(I)**\na high school diploma or a commensurate alternative award from a public or private high school;\n**(II)**\na General Education Development credential, a high school equivalency diploma recognized under State law, or another similar State-authorized credential;\n**(III)**\na credential or certificate from an area career and technical education school at the secondary level; or\n**(IV)**\na recognized postsecondary credential; or\n**(iv)**\nis enrolled in secondary school or in an education program assisting students in\u2014\n**(I)**\nobtaining a high school diploma or its recognized equivalent under State law;\n**(II)**\npassing the General Education Development test, a high school equivalence diploma examination, or other similar State-authorized exam;\n**(III)**\nobtaining a certificate or credential from an area career and technical education school providing education at the secondary level; or\n**(IV)**\nobtaining a recognized postsecondary credential.\n**(2) Waiver of grounds of inadmissibility**\nWith respect to any benefit under this title, and in addition to the waivers under subsection (c)(2), the Secretary may waive the grounds of inadmissibility under paragraph (1), (6)(E), (6)(G), or (10)(D) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) for humanitarian purposes, for family unity, or because the waiver is otherwise in the public interest.\n**(3) Application fee**\n**(A) In general**\nThe Secretary may, subject to an exemption under section 303(c), require an alien applying under this section to pay a reasonable fee that is commensurate with the cost of processing the application but does not exceed $495.00.\n**(B) Special procedures for applicants with DACA**\nThe Secretary shall establish a streamlined procedure for aliens who have been granted DACA and who meet the requirements for renewal (under the terms of the program in effect on January 1, 2017) to apply for adjustment of status to that of an alien lawfully admitted for permanent residence on a conditional basis under this section, or without the conditional basis as provided in section 104(c)(2). Such procedure shall not include a requirement that the applicant pay a fee, except that the Secretary may require an applicant who meets the requirements for lawful permanent residence without the conditional basis under section 104(c)(2) to pay a fee that is commensurate with the cost of processing the application, subject to the exemption under section 303(c).\n**(4) Background checks**\nThe Secretary may not grant an alien permanent resident status on a conditional basis under this section until the requirements of section 302 are satisfied.\n**(5) Military selective service**\nAn alien applying for permanent resident status on a conditional basis under this section, or without the conditional basis as provided in section 104(c)(2), shall establish that the alien has registered under the Military Selective Service Act ( 50 U.S.C. 3801 et seq. ), if the alien is subject to registration under such Act.\n##### (c) Criminal and national security bars\n**(1) Grounds of ineligibility**\nExcept as provided in paragraph (2), an alien is ineligible for adjustment of status under this title (whether on a conditional basis or without the conditional basis as provided in section 104(c)(2)) if any of the following apply:\n**(A)**\nThe alien is inadmissible under paragraph (2) or (3) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ).\n**(B)**\nExcluding any offense under State law for which an essential element is the alien\u2019s immigration status, and any minor traffic offense, the alien has been convicted of\u2014\n**(i)**\nany felony offense;\n**(ii)**\nthree or more misdemeanor offenses (excluding simple possession of cannabis or cannabis-related paraphernalia, any offense involving cannabis or cannabis-related paraphernalia which is no longer prosecutable in the State in which the conviction was entered, and any offense involving civil disobedience without violence) not occurring on the same date, and not arising out of the same act, omission, or scheme of misconduct; or\n**(iii)**\na misdemeanor offense of domestic violence, unless the alien demonstrates that such crime is related to the alien having been\u2014\n**(I)**\na victim of domestic violence, sexual assault, stalking, child abuse or neglect, abuse or neglect in later life, or human trafficking;\n**(II)**\nbattered or subjected to extreme cruelty; or\n**(III)**\na victim of criminal activity described in section 101(a)(15)(U)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(U)(iii) ).\n**(2) Waivers for certain misdemeanors**\nFor humanitarian purposes, family unity, or if otherwise in the public interest, the Secretary may\u2014\n**(A)**\nwaive the grounds of inadmissibility under subparagraphs (A), (C), and (D) of section 212(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(2) ), unless the conviction forming the basis for inadmissibility would otherwise render the alien ineligible under paragraph (1)(B) (subject to subparagraph (B)); and\n**(B)**\nfor purposes of clauses (ii) and (iii) of paragraph (1)(B), waive consideration of\u2014\n**(i)**\none misdemeanor offense if the alien has not been convicted of any offense in the 5-year period preceding the date on which the alien applies for adjustment of status under this title; or\n**(ii)**\nup to two misdemeanor offenses if the alien has not been convicted of any offense in the 10-year period preceding the date on which the alien applies for adjustment of status under this title.\n**(3) Authority to conduct secondary review**\n**(A) In general**\nNotwithstanding an alien\u2019s eligibility for adjustment of status under this title, and subject to the procedures described in this paragraph, the Secretary may, as a matter of non-delegable discretion, provisionally deny an application for adjustment of status (whether on a conditional basis or without the conditional basis as provided in section 104(c)(2)) if the Secretary, based on clear and convincing evidence, which shall include credible law enforcement information, determines that the alien is described in subparagraph (B) or (D).\n**(B) Public safety**\nAn alien is described in this subparagraph if\u2014\n**(i)**\nexcluding simple possession of cannabis or cannabis-related paraphernalia, any offense involving cannabis or cannabis-related paraphernalia which is no longer prosecutable in the State in which the conviction was entered, any offense under State law for which an essential element is the alien\u2019s immigration status, any offense involving civil disobedience without violence, and any minor traffic offense, the alien\u2014\n**(I)**\nhas been convicted of a misdemeanor offense punishable by a term of imprisonment of more than 30 days; or\n**(II)**\nhas been adjudicated delinquent in a State or local juvenile court proceeding that resulted in a disposition ordering placement in a secure facility; and\n**(ii)**\nthe alien poses a significant and continuing threat to public safety related to such conviction or adjudication.\n**(C) Public safety determination**\nFor purposes of subparagraph (B)(ii), the Secretary shall consider the recency of the conviction or adjudication; the length of any imposed sentence or placement; the nature and seriousness of the conviction or adjudication, including whether the elements of the offense include the unlawful possession or use of a deadly weapon to commit an offense or other conduct intended to cause serious bodily injury; and any mitigating factors pertaining to the alien\u2019s role in the commission of the offense.\n**(D) Gang participation**\nAn alien is described in this subparagraph if the alien has, within the 5 years immediately preceding the date of the application, knowingly, willfully, and voluntarily participated in offenses committed by a criminal street gang (as described in subsections (a) and (c) of section 521 of title 18, United States Code) with the intent to promote or further the commission of such offenses.\n**(E) Evidentiary limitation**\nFor purposes of subparagraph (D), allegations of gang membership obtained from a State or Federal in-house or local database, or a network of databases used for the purpose of recording and sharing activities of alleged gang members across law enforcement agencies, shall not establish the participation described in such paragraph.\n**(F) Notice**\n**(i) In general**\nPrior to rendering a discretionary decision under this paragraph, the Secretary shall provide written notice of the intent to provisionally deny the application to the alien (or the alien\u2019s counsel of record, if any) by certified mail and, if an electronic mail address is provided, by electronic mail (or other form of electronic communication). Such notice shall\u2014\n**(I)**\narticulate with specificity all grounds for the preliminary determination, including the evidence relied upon to support the determination; and\n**(II)**\nprovide the alien with not less than 90 days to respond.\n**(ii) Second notice**\nNot more than 30 days after the issuance of the notice under clause (i), the Secretary shall provide a second written notice that meets the requirements of such clause.\n**(iii) Notice not received**\nNotwithstanding any other provision of law, if an applicant provides good cause for not contesting a provisional denial under this paragraph, including a failure to receive notice as required under this subparagraph, the Secretary shall, upon a motion filed by the alien, reopen an application for adjustment of status under this title and allow the applicant an opportunity to respond, consistent with clause (i)(II).\n**(G) Judicial review of a provisional denial**\n**(i) In general**\nNotwithstanding any other provision of law, if, after notice and the opportunity to respond under subparagraph (F), the Secretary provisionally denies an application for adjustment of status under this Act, the alien shall have 60 days from the date of the Secretary\u2019s determination to seek review of such determination in an appropriate United States district court.\n**(ii) Scope of review and decision**\nNotwithstanding any other provision of law, review under paragraph (1) shall be de novo and based solely on the administrative record, except that the applicant shall be given the opportunity to supplement the administrative record and the Secretary shall be given the opportunity to rebut the evidence and arguments raised in such submission. Upon issuing its decision, the court shall remand the matter, with appropriate instructions, to the Department of Homeland Security to render a final decision on the application.\n**(iii) Appointed counsel**\nNotwithstanding any other provision of law, an applicant seeking judicial review under clause (i) shall be represented by counsel. Upon the request of the applicant, counsel shall be appointed for the applicant, in accordance with procedures to be established by the Attorney General within 90 days of the date of the enactment of this Act, and shall be funded in accordance with fees collected and deposited in the Immigration Counsel Account under section 312.\n**(4) Definitions**\nFor purposes of this subsection\u2014\n**(A)**\nthe term felony offense means an offense under Federal or State law that is punishable by a maximum term of imprisonment of more than 1 year;\n**(B)**\nthe term misdemeanor offense means an offense under Federal or State law that is punishable by a term of imprisonment of more than 5 days but not more than 1 year; and\n**(C)**\nthe term crime of domestic violence means any offense that has as an element the use, attempted use, or threatened use of physical force against a person committed by a current or former spouse of the person, by an individual with whom the person shares a child in common, by an individual who is cohabiting with or has cohabited with the person as a spouse, by an individual similarly situated to a spouse of the person under the domestic or family violence laws of the jurisdiction where the offense occurs, or by any other individual against a person who is protected from that individual\u2019s acts under the domestic or family violence laws of the United States or any State, Indian Tribal government, or unit of local government.\n##### (d) Limitation on removal of certain alien minors\nAn alien who is 18 years of age or younger and meets the requirements under subparagraphs (A), (B), and (C) of subsection (b)(1) shall be provided a reasonable opportunity to meet the educational requirements under subparagraph (D) of such subsection. The Attorney General or the Secretary may not commence or continue with removal proceedings against such an alien.\n##### (e) Withdrawal of application\nThe Secretary shall, upon receipt of a request to withdraw an application for adjustment of status under this section, cease processing of the application, and close the case. Withdrawal of the application under this subsection shall not prejudice any future application filed by the applicant for any immigration benefit under this title or under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n#### 103. Terms of permanent resident status on a conditional basis\n##### (a) Period of status\nPermanent resident status on a conditional basis is\u2014\n**(1)**\nvalid for a period of 10 years, unless such period is extended by the Secretary; and\n**(2)**\nsubject to revocation under subsection (c).\n##### (b) Notice of requirements\nAt the time an alien obtains permanent resident status on a conditional basis, the Secretary shall provide notice to the alien regarding the provisions of this title and the requirements to have the conditional basis of such status removed.\n##### (c) Revocation of status\nThe Secretary may revoke the permanent resident status on a conditional basis of an alien only if the Secretary\u2014\n**(1)**\ndetermines that the alien ceases to meet the requirements under section 102(b)(1)(C); and\n**(2)**\nprior to the revocation, provides the alien\u2014\n**(A)**\nnotice of the proposed revocation; and\n**(B)**\nthe opportunity for a hearing to provide evidence that the alien meets such requirements or otherwise to contest the proposed revocation.\n##### (d) Return to previous immigration status\nAn alien whose permanent resident status on a conditional basis expires under subsection (a)(1) or is revoked under subsection (c), shall return to the immigration status that the alien had immediately before receiving permanent resident status on a conditional basis.\n#### 104. Removal of conditional basis of permanent resident status\n##### (a) Eligibility for removal of conditional basis\n**(1) In general**\nSubject to paragraph (2), the Secretary shall remove the conditional basis of an alien\u2019s permanent resident status granted under this title and grant the alien status as an alien lawfully admitted for permanent residence if the alien\u2014\n**(A)**\nis described in section 102(b)(1)(C);\n**(B)**\nhas not abandoned the alien\u2019s residence in the United States during the period in which the alien has permanent resident status on a conditional basis; and\n**(C)**\n**(i)**\nhas obtained a degree from an institution of higher education, or has completed at least 2 years, in good standing, of a program in the United States leading to a bachelor\u2019s degree or higher degree or a recognized postsecondary credential from an area career and technical education school providing education at the postsecondary level;\n**(ii)**\nhas served in the Uniformed Services for at least 2 years and, if discharged, received an honorable discharge; or\n**(iii)**\ndemonstrates earned income for periods totaling at least 3 years and at least 75 percent of the time that the alien has had a valid employment authorization, except that, in the case of an alien who was enrolled in an institution of higher education, an area career and technical education school to obtain a recognized postsecondary credential, or an education program described in section 102(b)(1)(D)(iii), the Secretary shall reduce such total 3-year requirement by the total of such periods of enrollment.\n**(2) Hardship exception**\nThe Secretary shall remove the conditional basis of an alien\u2019s permanent resident status and grant the alien status as an alien lawfully admitted for permanent residence if the alien\u2014\n**(A)**\nsatisfies the requirements under subparagraphs (A) and (B) of paragraph (1);\n**(B)**\ndemonstrates compelling circumstances for the inability to satisfy the requirements under subparagraph (C) of such paragraph; and\n**(C)**\ndemonstrates that\u2014\n**(i)**\nthe alien has a disability;\n**(ii)**\nthe alien is a full-time caregiver; or\n**(iii)**\nthe removal of the alien from the United States would result in hardship to the alien or the alien\u2019s spouse, parent, or child who is a national of the United States or is lawfully admitted for permanent residence.\n**(3) Citizenship requirement**\n**(A) In general**\nExcept as provided in subparagraph (B), the conditional basis of an alien\u2019s permanent resident status granted under this title may not be removed unless the alien demonstrates that the alien satisfies the requirements under section 312(a) of the Immigration and Nationality Act ( 8 U.S.C. 1423(a) ).\n**(B) Exception**\nSubparagraph (A) shall not apply to an alien who is unable to meet the requirements under such section 312(a) due to disability.\n**(4) Application fee**\nThe Secretary may, subject to an exemption under section 303(c), require aliens applying for removal of the conditional basis of an alien\u2019s permanent resident status under this section to pay a reasonable fee that is commensurate with the cost of processing the application.\n**(5) Background checks**\nThe Secretary may not remove the conditional basis of an alien\u2019s permanent resident status until the requirements of section 302 are satisfied.\n##### (b) Treatment for purposes of naturalization\n**(1) In general**\nFor purposes of title III of the Immigration and Nationality Act ( 8 U.S.C. 1401 et seq. ), an alien granted permanent resident status on a conditional basis shall be considered to have been admitted to the United States, and be present in the United States, as an alien lawfully admitted for permanent residence.\n**(2) Limitation on application for naturalization**\nAn alien may not apply for naturalization while the alien is in permanent resident status on a conditional basis.\n##### (c) Timing of approval of lawful permanent resident status\n**(1) In general**\nAn alien granted permanent resident status on a conditional basis under this title may apply to have such conditional basis removed at any time after such alien has met the eligibility requirements set forth in subsection (a).\n**(2) Approval with regard to initial applications**\n**(A) In general**\nNotwithstanding any other provision of law, the Secretary or the Attorney General shall adjust to the status of an alien lawfully admitted for permanent resident status without conditional basis, any alien who\u2014\n**(i)**\ndemonstrates eligibility for lawful permanent residence status on a conditional basis under section 102(b); and\n**(ii)**\nsubject to the exceptions described in subsections (a)(2) and (a)(3)(B) of this section, already has fulfilled the requirements of paragraphs (1) and (3) of subsection (a) of this section at the time such alien first submits an application for benefits under this title.\n**(B) Background checks**\nSubsection (a)(5) shall apply to an alien seeking lawful permanent resident status without conditional basis in an initial application in the same manner as it applies to an alien seeking removal of the conditional basis of an alien\u2019s permanent resident status. Section 102(b)(4) shall not be construed to require the Secretary to conduct more than one identical security or law enforcement background check on such an alien.\n**(C) Application fees**\nIn the case of an alien seeking lawful permanent resident status without conditional basis in an initial application, the alien shall pay the fee required under subsection (a)(4), subject to the exemption allowed under section 303(c), but shall not be required to pay the application fee under section 102(b)(3).\n#### 105. Restoration of State option to determine residency for purposes of higher education benefits\n##### (a) In general\nSection 505 of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1623 ) is repealed.\n##### (b) Effective date\nThe repeal under subsection (a) shall take effect as if included in the original enactment of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 (division C of Public Law 104\u2013208 ; 110 Stat. 3009\u2013546).\nII\nAmerican Promise Act of 2025\n#### 201. Short title\nThis title may be cited as the American Promise Act of 2025 .\n#### 202. Adjustment of status for certain nationals of certain countries designated for temporary protected status or deferred enforced departure\n##### (a) In general\nNotwithstanding any other provision of law, the Secretary or the Attorney General shall adjust to the status of an alien lawfully admitted for permanent residence, an alien described in subsection (b) if the alien\u2014\n**(1)**\napplies for such adjustment, including submitting any required documents under section 307, not later than 3 years after the date of the enactment of this Act;\n**(2)**\nhas been continuously physically present in the United States for a period of not less than 3 years; and\n**(3)**\nsubject to subsection (c), is not inadmissible under paragraph (1), (2), (3), (6)(D), (6)(E), (6)(F), (6)(G), (8), or (10) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ).\n##### (b) Aliens eligible for adjustment of status\nAn alien shall be eligible for adjustment of status under this section if the alien is an individual\u2014\n**(1)**\nwho\u2014\n**(A)**\nis a national of a foreign state (or part thereof) (or in the case of an alien having no nationality, is a person who last habitually resided in such state) with a designation under subsection (b) of section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b) ) on January 1, 2017, who had or was otherwise eligible for temporary protected status on such date notwithstanding subsections (c)(1)(A)(iv) and (c)(3)(C) of such section; and\n**(B)**\nhas not engaged in conduct since such date that would render the alien ineligible for temporary protected status under section 244(c)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1245a(c)(2) ); or\n**(2)**\nwho was eligible for Deferred Enforced Departure as of January 20, 2021, and has not engaged in conduct since that date that would render the alien ineligible for Deferred Enforced Departure.\n##### (c) Waiver of grounds of inadmissibility\n**(1) In general**\nExcept as provided in paragraph (2), with respect to any benefit under this title, and in addition to any waivers that are otherwise available, the Secretary may waive the grounds of inadmissibility under paragraph (1), subparagraphs (A), (C), and (D) of paragraph (2), subparagraphs (D) through (G) of paragraph (6), or paragraph (10)(D) of section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) for humanitarian purposes, for family unity, or because the waiver is otherwise in the public interest.\n**(2) Exception**\nThe Secretary may not waive a ground described in paragraph (1) if such inadmissibility is based on a conviction or convictions, and such conviction or convictions would otherwise render the alien ineligible under section 244(c)(2)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(c)(2)(B) ).\n##### (d) Application\n**(1) Fee**\nThe Secretary shall, subject to an exemption under section 303(c), require an alien applying for adjustment of status under this section to pay a reasonable fee that is commensurate with the cost of processing the application, but does not exceed $1,140.\n**(2) Background checks**\nThe Secretary may not grant an alien permanent resident status on a conditional basis under this section until the requirements of section 302 are satisfied.\n**(3) Withdrawal of application**\nThe Secretary of Homeland Security shall, upon receipt of a request to withdraw an application for adjustment of status under this section, cease processing of the application and close the case. Withdrawal of the application under this subsection shall not prejudice any future application filed by the applicant for any immigration benefit under this title or under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n#### 203. Clarification\nSection 244(f)(4) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(f)(4) ) is amended by inserting after considered the following: as having been inspected and admitted into the United States, and .\nIII\nGeneral Provisions\n#### 301. Definitions\n##### (a) In general\nIn this Act:\n**(1) In general**\nExcept as otherwise specifically provided, any term used in this Act that is used in the immigration laws shall have the meaning given such term in the immigration laws.\n**(2) Appropriate United States district court**\nThe term appropriate United States district court means the United States District Court for the District of Columbia or the United States district court with jurisdiction over the alien\u2019s principal place of residence.\n**(3) Area career and technical education school**\nThe term area career and technical education school has the meaning given such term in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ).\n**(4) DACA**\nThe term DACA means deferred action granted to an alien pursuant to the Deferred Action for Childhood Arrivals policy announced by the Secretary of Homeland Security on June 15, 2012.\n**(5) Disability**\nThe term disability has the meaning given such term in section 3(1) of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102(1) ).\n**(6) Federal poverty line**\nThe term Federal poverty line has the meaning given such term in section 213A(h) of the Immigration and Nationality Act ( 8 U.S.C. 1183a ).\n**(7) High school; secondary school**\nThe terms high school and secondary school have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(8) Immigration laws**\nThe term immigration laws has the meaning given such term in section 101(a)(17) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(17) ).\n**(9) Institution of higher education**\nThe term institution of higher education \u2014\n**(A)**\nexcept as provided in subparagraph (B), has the meaning given such term in section 102 of the Higher Education Act of 1965 ( 20 U.S.C. 1002 ); and\n**(B)**\ndoes not include an institution of higher education outside of the United States.\n**(10) Recognized postsecondary credential**\nThe term recognized postsecondary credential has the meaning given such term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(11) Secretary**\nExcept as otherwise specifically provided, the term Secretary means the Secretary of Homeland Security.\n**(12) Uniformed services**\nThe term Uniformed Services has the meaning given the term uniformed services in section 101(a) of title 10, United States Code.\n##### (b) Treatment of expunged convictions\nFor purposes of adjustment of status under this Act, the terms convicted and conviction , as used in this Act and in sections 212 and 244 of the Immigration and Nationality Act ( 8 U.S.C. 1182 , 1254a), do not include a judgment that has been expunged or set aside, that resulted in a rehabilitative disposition, or the equivalent.\n#### 302. Submission of biometric and biographic data; background checks\n##### (a) Submission of biometric and biographic data\nThe Secretary may not grant an alien adjustment of status under this Act, on either a conditional or permanent basis, unless the alien submits biometric and biographic data, in accordance with procedures established by the Secretary. The Secretary shall provide an alternative procedure for aliens who are unable to provide such biometric or biographic data because of a physical impairment.\n##### (b) Background checks\nThe Secretary shall use biometric, biographic, and other data that the Secretary determines appropriate to conduct security and law enforcement background checks and to determine whether there is any criminal, national security, or other factor that would render the alien ineligible for adjustment of status under this Act, on either a conditional or permanent basis. The status of an alien may not be adjusted, on either a conditional or permanent basis, unless security and law enforcement background checks are completed to the satisfaction of the Secretary.\n#### 303. Limitation on removal; application and fee exemption; and other conditions on eligible individuals\n##### (a) Limitation on removal\nAn alien who appears to be prima facie eligible for relief under this Act shall be given a reasonable opportunity to apply for such relief and may not be removed until, subject to section 306(c)(2), a final decision establishing ineligibility for relief is rendered.\n##### (b) Application\nAn alien present in the United States who has been ordered removed or has been permitted to depart voluntarily from the United States may, notwithstanding such order or permission to depart, apply for adjustment of status under this Act. Such alien shall not be required to file a separate motion to reopen, reconsider, or vacate the order of removal. If the Secretary approves the application, the Secretary shall cancel the order of removal. If the Secretary renders a final administrative decision to deny the application, the order of removal or permission to depart shall be effective and enforceable to the same extent as if the application had not been made, only after all available administrative and judicial remedies have been exhausted.\n##### (c) Fee exemption\nAn applicant may be exempted from paying an application fee required under this Act if the applicant\u2014\n**(1)**\nis 18 years of age or younger;\n**(2)**\nreceived total income, during the 12-month period immediately preceding the date on which the applicant files an application under this Act, that is less than 150 percent of the Federal poverty line;\n**(3)**\nis in foster care or otherwise lacks any parental or other familial support; or\n**(4)**\ncannot care for himself or herself because of a serious, chronic disability.\n##### (d) Advance parole\nDuring the period beginning on the date on which an alien applies for adjustment of status under this Act and ending on the date on which the Secretary makes a final decision regarding such application, the alien shall be eligible to apply for advance parole. Section 101(g) of the Immigration and Nationality Act ( 8 U.S.C. 1101(g) ) shall not apply to an alien granted advance parole under this Act.\n##### (e) Employment\nAn alien whose removal is stayed pursuant to this Act, who may not be placed in removal proceedings pursuant to this Act, or who has pending an application under this Act, shall, upon application to the Secretary, be granted an employment authorization document.\n#### 304. Determination of continuous presence and residence\n##### (a) Effect of notice To appear\nAny period of continuous physical presence or continuous residence in the United States of an alien who applies for permanent resident status under this Act (whether on a conditional basis or without the conditional basis as provided in section 104(c)(2)) shall not terminate when the alien is served a notice to appear under section 239(a) of the Immigration and Nationality Act ( 8 U.S.C. 1229(a) ).\n##### (b) Treatment of certain breaks in presence or residence\n**(1) In general**\nExcept as provided in paragraphs (2) and (3), an alien shall be considered to have failed to maintain\u2014\n**(A)**\ncontinuous physical presence in the United States under this Act if the alien has departed from the United States for any period exceeding 90 days or for any periods, in the aggregate, exceeding 180 days; and\n**(B)**\ncontinuous residence in the United States under this Act if the alien has departed from the United States for any period exceeding 180 days, unless the alien establishes to the satisfaction of the Secretary of Homeland Security that the alien did not in fact abandon residence in the United States during such period.\n**(2) Extensions for extenuating circumstances**\nThe Secretary may extend the time periods described in paragraph (1) for an alien who demonstrates that the failure to timely return to the United States was due to extenuating circumstances beyond the alien\u2019s control, including\u2014\n**(A)**\nthe serious illness of the alien;\n**(B)**\ndeath or serious illness of a parent, grandparent, sibling, or child of the alien;\n**(C)**\nprocessing delays associated with the application process for a visa or other travel document; or\n**(D)**\nrestrictions on international travel due to the public health emergency declared by the Secretary of Health and Human Services under section 319 of the Public Health Service Act ( 42 U.S.C. 247d ) with respect to COVID\u201319.\n**(3) Travel authorized by the secretary**\nAny period of travel outside of the United States by an alien that was authorized by the Secretary may not be counted toward any period of departure from the United States under paragraph (1).\n##### (c) Waiver of physical presence\nWith respect to aliens who were removed or departed the United States on or after January 20, 2017, and who were continuously physically present in the United States for at least 4 years prior to such removal or departure, the Secretary may, as a matter of discretion, waive the physical presence requirement under section 102(b)(1)(A) or section 202(a)(2) for humanitarian purposes, for family unity, or because a waiver is otherwise in the public interest. The Secretary, in consultation with the Secretary of State, shall establish a procedure for such aliens to apply for relief under section 102 or 202 from outside the United States if they would have been eligible for relief under such section, but for their removal or departure.\n#### 305. Exemption from numerical limitations\nNothing in this Act or in any other law may be construed to apply a numerical limitation on the number of aliens who may be granted permanent resident status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)).\n#### 306. Availability of administrative and judicial review\n##### (a) Administrative review\nNot later than 30 days after the date of the enactment of this Act, the Secretary shall provide to aliens who have applied for adjustment of status under this Act a process by which an applicant may seek administrative appellate review of a denial of an application for adjustment of status, or a revocation of such status.\n##### (b) Judicial review\nExcept as provided in subsection (c), and notwithstanding any other provision of law, an alien may seek judicial review of a denial of an application for adjustment of status, or a revocation of such status, under this Act in an appropriate United States district court.\n##### (c) Stay of removal\n**(1) In general**\nExcept as provided in paragraph (2), an alien seeking administrative or judicial review under this Act may not be removed from the United States until a final decision is rendered establishing that the alien is ineligible for adjustment of status under this Act.\n**(2) Exception**\nThe Secretary may remove an alien described in paragraph (1) pending judicial review if such removal is based on criminal or national security grounds described in this Act. Such removal shall not affect the alien\u2019s right to judicial review under this Act. The Secretary shall promptly return a removed alien if a decision to deny an application for adjustment of status under this Act, or to revoke such status, is reversed.\n#### 307. Documentation requirements\n##### (a) Documents establishing identity\nAn alien\u2019s application for permanent resident status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)) may include, as evidence of identity, the following:\n**(1)**\nA passport or national identity document from the alien\u2019s country of origin that includes the alien\u2019s name and the alien\u2019s photograph or fingerprint.\n**(2)**\nThe alien\u2019s birth certificate and an identity card that includes the alien\u2019s name and photograph.\n**(3)**\nA school identification card that includes the alien\u2019s name and photograph, and school records showing the alien\u2019s name and that the alien is or was enrolled at the school.\n**(4)**\nA Uniformed Services identification card issued by the Department of Defense.\n**(5)**\nAny immigration or other document issued by the United States Government bearing the alien\u2019s name and photograph.\n**(6)**\nA State-issued identification card bearing the alien\u2019s name and photograph.\n**(7)**\nAny other evidence determined to be credible by the Secretary.\n##### (b) Documents establishing entry, continuous physical presence, lack of abandonment of residence\nTo establish that an alien was 18 years of age or younger on the date on which the alien entered the United States, and has continuously resided in the United States since such entry, as required under section 102(b)(1)(B), that an alien has been continuously physically present in the United States, as required under section 102(b)(1)(A) or 202(a)(2), or that an alien has not abandoned residence in the United States, as required under section 104(a)(1)(B), the alien may submit the following forms of evidence:\n**(1)**\nPassport entries, including admission stamps on the alien\u2019s passport.\n**(2)**\nAny document from the Department of Justice or the Department of Homeland Security noting the alien\u2019s date of entry into the United States.\n**(3)**\nRecords from any educational institution the alien has attended in the United States.\n**(4)**\nEmployment records of the alien that include the employer\u2019s name and contact information, or other records demonstrating earned income.\n**(5)**\nRecords of service from the Uniformed Services.\n**(6)**\nOfficial records from a religious entity confirming the alien\u2019s participation in a religious ceremony.\n**(7)**\nA birth certificate for a child who was born in the United States.\n**(8)**\nHospital or medical records showing medical treatment or hospitalization, the name of the medical facility or physician, and the date of the treatment or hospitalization.\n**(9)**\nAutomobile license receipts or registration.\n**(10)**\nDeeds, mortgages, or rental agreement contracts.\n**(11)**\nRent receipts or utility bills bearing the alien\u2019s name or the name of an immediate family member of the alien, and the alien\u2019s address.\n**(12)**\nTax receipts.\n**(13)**\nInsurance policies.\n**(14)**\nRemittance records, including copies of money order receipts sent in or out of the country.\n**(15)**\nTravel records.\n**(16)**\nDated bank transactions.\n**(17)**\nTwo or more sworn affidavits from individuals who are not related to the alien who have direct knowledge of the alien\u2019s continuous physical presence in the United States, that contain\u2014\n**(A)**\nthe name, address, and telephone number of the affiant; and\n**(B)**\nthe nature and duration of the relationship between the affiant and the alien.\n**(18)**\nAny other evidence determined to be credible by the Secretary.\n##### (c) Documents establishing admission to an institution of higher education\nTo establish that an alien has been admitted to an institution of higher education, the alien may submit to the Secretary a document from the institution of higher education certifying that the alien\u2014\n**(1)**\nhas been admitted to the institution; or\n**(2)**\nis currently enrolled in the institution as a student.\n##### (d) Documents establishing receipt of a degree from an institution of higher education\nTo establish that an alien has acquired a degree from an institution of higher education in the United States, the alien may submit to the Secretary a diploma or other document from the institution stating that the alien has received such a degree.\n##### (e) Documents establishing receipt of a high school diploma, general educational development credential, or a recognized equivalent\nTo establish that in the United States an alien has earned a high school diploma or a commensurate alternative award from a public or private high school, has obtained the General Education Development credential, or otherwise has satisfied section 102(b)(1)(D)(iii), the alien may submit to the Secretary the following:\n**(1)**\nA high school diploma, certificate of completion, or other alternate award.\n**(2)**\nA high school equivalency diploma or certificate recognized under State law.\n**(3)**\nEvidence that the alien passed a State-authorized exam, including the General Education Development test, in the United States.\n**(4)**\nEvidence that the alien successfully completed an area career and technical education program, such as a certification, certificate, or similar alternate award.\n**(5)**\nEvidence that the alien obtained a recognized postsecondary credential.\n**(6)**\nAny other evidence determined to be credible by the Secretary.\n##### (f) Documents establishing enrollment in an educational program\nTo establish that an alien is enrolled in any school or education program described in section 102(b)(1)(D)(iv) or 104(a)(1)(C), the alien may submit school records from the United States school that the alien is currently attending that include\u2014\n**(1)**\nthe name of the school; and\n**(2)**\nthe alien\u2019s name, periods of attendance, and current grade or educational level.\n##### (g) Documents establishing exemption from application fees\nTo establish that an alien is exempt from an application fee under this Act, the alien may submit to the Secretary the following relevant documents:\n**(1) Documents to establish age**\nTo establish that an alien meets an age requirement, the alien may provide proof of identity, as described in subsection (a), that establishes that the alien is 18 years of age or younger.\n**(2) Documents to establish income**\nTo establish the alien\u2019s income, the alien may provide\u2014\n**(A)**\nemployment records or other records of earned income, including records that have been maintained by the Social Security Administration, the Internal Revenue Service, or any other Federal, State, or local government agency;\n**(B)**\nbank records; or\n**(C)**\nat least two sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the alien\u2019s work and income that contain\u2014\n**(i)**\nthe name, address, and telephone number of the affiant; and\n**(ii)**\nthe nature and duration of the relationship between the affiant and the alien.\n**(3) Documents to establish foster care, lack of familial support, or serious, chronic disability**\nTo establish that the alien is in foster care, lacks parental or familial support, or has a serious, chronic disability, the alien may provide at least two sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the circumstances that contain\u2014\n**(A)**\na statement that the alien is in foster care, otherwise lacks any parental or other familiar support, or has a serious, chronic disability, as appropriate;\n**(B)**\nthe name, address, and telephone number of the affiant; and\n**(C)**\nthe nature and duration of the relationship between the affiant and the alien.\n##### (h) Documents establishing qualification for hardship exemption\nTo establish that an alien satisfies one of the criteria for the hardship exemption set forth in section 104(a)(2)(C), the alien may submit to the Secretary at least two sworn affidavits from individuals who are not related to the alien and who have direct knowledge of the circumstances that warrant the exemption, that contain\u2014\n**(1)**\nthe name, address, and telephone number of the affiant; and\n**(2)**\nthe nature and duration of the relationship between the affiant and the alien.\n##### (i) Documents establishing service in the uniformed services\nTo establish that an alien has served in the Uniformed Services for at least 2 years and, if discharged, received an honorable discharge, the alien may submit to the Secretary\u2014\n**(1)**\na Department of Defense form DD\u2013214;\n**(2)**\na National Guard Report of Separation and Record of Service form 22;\n**(3)**\npersonnel records for such service from the appropriate Uniformed Service; or\n**(4)**\nhealth records from the appropriate Uniformed Service.\n##### (j) Documents establishing earned income\n**(1) In general**\nAn alien may satisfy the earned income requirement under section 104(a)(1)(C)(iii) by submitting records that\u2014\n**(A)**\nestablish compliance with such requirement; and\n**(B)**\nhave been maintained by the Social Security Administration, the Internal Revenue Service, or any other Federal, State, or local government agency.\n**(2) Other documents**\nAn alien who is unable to submit the records described in paragraph (1) may satisfy the earned income requirement by submitting at least two types of reliable documents that provide evidence of employment or other forms of earned income, including\u2014\n**(A)**\nbank records;\n**(B)**\nbusiness records;\n**(C)**\nemployer or contractor records;\n**(D)**\nrecords of a labor union, day labor center, or organization that assists workers in employment;\n**(E)**\nsworn affidavits from individuals who are not related to the alien and who have direct knowledge of the alien\u2019s work, that contain\u2014\n**(i)**\nthe name, address, and telephone number of the affiant; and\n**(ii)**\nthe nature and duration of the relationship between the affiant and the alien;\n**(F)**\nremittance records; or\n**(G)**\nany other evidence determined to be credible by the Secretary.\n##### (k) Authority To prohibit use of certain documents\nIf the Secretary determines, after publication in the Federal Register and an opportunity for public comment, that any document or class of documents does not reliably establish identity or that permanent resident status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)) is being obtained fraudulently to an unacceptable degree, the Secretary may prohibit or restrict the use of such document or class of documents.\n#### 308. Rulemaking\n##### (a) In general\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall publish in the Federal Register interim final rules implementing this Act, which shall allow eligible individuals to immediately apply for relief under this Act. Notwithstanding section 553 of title 5, United States Code, the regulation shall be effective, on an interim basis, immediately upon publication, but may be subject to change and revision after public notice and opportunity for a period of public comment. The Secretary shall finalize such rules not later than 180 days after the date of publication.\n##### (b) Paperwork reduction act\nThe requirements under chapter 35 of title 44, United States Code, (commonly known as the Paperwork Reduction Act ) shall not apply to any action to implement this Act.\n#### 309. Confidentiality of information\n##### (a) In general\nThe Secretary may not disclose or use information (including information provided during administrative or judicial review) provided in applications filed under this Act or in requests for DACA for the purpose of immigration enforcement.\n##### (b) Referrals prohibited\nThe Secretary, based solely on information provided in an application for adjustment of status under this Act (including information provided during administrative or judicial review) or an application for DACA, may not refer an applicant to U.S. Immigration and Customs Enforcement, U.S. Customs and Border Protection, or any designee of either such entity.\n##### (c) Limited exception\nNotwithstanding subsections (a) and (b), information provided in an application for adjustment of status under this Act may be shared with Federal security and law enforcement agencies\u2014\n**(1)**\nfor assistance in the consideration of an application for adjustment of status under this Act;\n**(2)**\nto identify or prevent fraudulent claims;\n**(3)**\nfor national security purposes; or\n**(4)**\nfor the investigation or prosecution of any felony offense not related to immigration status.\n##### (d) Penalty\nAny person who knowingly uses, publishes, or permits information to be examined in violation of this section shall be fined not more than $10,000.\n#### 310. Grant program to assist eligible applicants\n##### (a) Establishment\nThe Secretary shall establish, within U.S. Citizenship and Immigration Services, a program to award grants, on a competitive basis, to eligible nonprofit organizations that will use the funding to assist eligible applicants under this Act by providing them with the services described in subsection (b).\n##### (b) Use of funds\nGrant funds awarded under this section shall be used for the design and implementation of programs that provide\u2014\n**(1)**\ninformation to the public regarding the eligibility and benefits of permanent resident status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)), particularly to individuals potentially eligible for such status;\n**(2)**\nassistance, within the scope of authorized practice of immigration law, to individuals submitting applications for adjustment of status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)), including\u2014\n**(A)**\nscreening prospective applicants to assess their eligibility for such status;\n**(B)**\ncompleting applications and petitions, including providing assistance in obtaining the requisite documents and supporting evidence; and\n**(C)**\nproviding any other assistance that the Secretary or grantee considers useful or necessary to apply for adjustment of status under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)); and\n**(3)**\nassistance, within the scope of authorized practice of immigration law, and instruction, to individuals\u2014\n**(A)**\non the rights and responsibilities of United States citizenship;\n**(B)**\nin civics and English as a second language;\n**(C)**\nin preparation for the General Education Development test; and\n**(D)**\nin applying for adjustment of status and United States citizenship.\n##### (c) Authorization of appropriations\n**(1) Amounts authorized**\nThere are authorized to be appropriated such sums as may be necessary for each of the fiscal years 2026 through 2036 to carry out this section.\n**(2) Availability**\nAny amounts appropriated pursuant to paragraph (1) shall remain available until expended.\n#### 311. Provisions affecting eligibility for adjustment of status\nAn alien\u2019s eligibility to be lawfully admitted for permanent residence under this Act (whether on a conditional basis, or without the conditional basis as provided in section 104(c)(2)) shall not preclude the alien from seeking any status under any other provision of law for which the alien may otherwise be eligible.\n#### 312. Supplementary surcharge for appointed counsel\n##### (a) In general\nExcept as provided in section 302 and in cases where the applicant is exempt from paying a fee under section 303(c), in any case in which a fee is charged pursuant to this Act, an additional surcharge of $25 shall be imposed and collected for the purpose of providing appointed counsel to applicants seeking judicial review of the Secretary\u2019s decision to provisionally deny an application under this Act.\n##### (b) Immigration counsel account\nThere is established in the general fund of the Treasury a separate account which shall be known as the Immigration Counsel Account . Fees collected under subsection (a) shall be deposited into the Immigration Counsel Account and shall remain available until expended for purposes of providing appointed counsel as required under this Act.\n##### (c) Report\nAt the end of each 2-year period, beginning with the establishment of this account, the Secretary of Homeland Security shall submit a report to the Congress concerning the status of the account, including any balances therein, and recommend any adjustment in the prescribed fee that may be required to ensure that the receipts collected from the fee charged for the succeeding two years equal, as closely as possible, the cost of providing appointed counsel as required under this Act.\n#### 313. Annual report on provisional denial authority\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Secretary of Homeland Security shall submit to the Congress a report detailing the number of applicants that receive\u2014\n**(1)**\na provisional denial under this Act;\n**(2)**\na final denial under this Act without seeking judicial review;\n**(3)**\na final denial under this Act after seeking judicial review; and\n**(4)**\nan approval under this Act after seeking judicial review.",
      "versionDate": "2025-02-26",
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
        "name": "Immigration",
        "updateDate": "2025-03-18T14:10:50Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1589ih.xml"
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
      "title": "American Dream and Promise Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Dream and Promise Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Promise Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dream Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-03-17T12:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the cancellation of removal and adjustment of status of certain aliens, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:44Z"
    }
  ]
}
```
