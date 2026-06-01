# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8074?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8074
- Title: Kira Johnson Act
- Congress: 119
- Bill type: HR
- Bill number: 8074
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-23T08:07:13Z
- Update date including text: 2026-04-23T08:07:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8074",
    "number": "8074",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000370",
        "district": "12",
        "firstName": "Alma",
        "fullName": "Rep. Adams, Alma S. [D-NC-12]",
        "lastName": "Adams",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Kira Johnson Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:13Z",
    "updateDateIncludingText": "2026-04-23T08:07:13Z"
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
          "date": "2026-03-25T14:02:05Z",
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
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "GA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "VA"
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
      "sponsorshipDate": "2026-03-25",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
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
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "OH"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "OR"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "GA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8074ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8074\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Ms. Adams (for herself, Ms. Underwood , Mrs. McIver , Ms. Tlaib , Ms. Norton , Ms. Moore of Wisconsin , Mrs. Watson Coleman , Ms. Kamlager-Dove , Mr. Johnson of Georgia , Ms. Pressley , Mr. Ivey , Mr. Krishnamoorthi , Mrs. Cherfilus-McCormick , Mr. Menefee , Mr. Bell , Mr. Moulton , Ms. Clarke of New York , Ms. DelBene , Mr. Garamendi , Mr. Cohen , Ms. Stansbury , Mrs. Dingell , Ms. Jacobs , Mr. Figures , Mr. Horsford , Mr. Garc\u00eda of Illinois , Mr. Veasey , Mrs. Beatty , Mr. Smith of Washington , Ms. Sewell , Ms. Wilson of Florida , Mr. Jackson of Illinois , Mr. Conaway , Mr. Scott of Virginia , Mrs. Hayes , Ms. Craig , Mr. McGarvey , Mrs. Grijalva , Mr. Carson , Mr. Takano , Mrs. McBath , Mr. Latimer , Ms. Johnson of Texas , Mr. Soto , Mr. David Scott of Georgia , Ms. Barrag\u00e1n , Ms. McClellan , Mr. Schneider , Mr. Mullin , Ms. Strickland , Mr. Tonko , Ms. Dean of Pennsylvania , Mrs. Sykes , Ms. Salinas , Mr. Lieu , and Ms. Scanlon ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo end preventable maternal mortality and severe maternal morbidity in the United States and close disparities in maternal health outcomes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Kira Johnson Act .\n#### 2. Sustained funding for community-based organizations to advance maternal health equity\n##### (a) In general\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall award grants to eligible entities to establish or expand programs to advance maternal health equity.\n##### (b) Timing\nFollowing the 1-year period described in subsection (d), the Secretary shall commence awarding the grants authorized by subsection (a).\n##### (c) Eligible entities\nTo be eligible to seek a grant under this section, an entity shall be a community-based organization offering programs and resources aligned with evidence-based practices for improving maternal health outcomes for demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n##### (d) Outreach and technical assistance period\nDuring the 1-year period beginning on the date of enactment of this Act, the Secretary shall\u2014\n**(1)**\nconduct outreach to encourage eligible entities to apply for grants under this section; and\n**(2)**\nprovide technical assistance to eligible entities on best practices for applying for grants under this section.\n##### (e) Special consideration\n**(1) Outreach**\nIn conducting outreach under subsection (d), the Secretary shall give special consideration to eligible entities that\u2014\n**(A)**\nare based in, and provide support for, communities with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes, to the extent such data are available;\n**(B)**\nare led by individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes; and\n**(C)**\noffer programs and resources that are aligned with evidence-based practices for improving maternal health outcomes for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n**(2) Awards**\nIn awarding grants under this section, the Secretary shall give special consideration to eligible entities that\u2014\n**(A)**\nare described in subparagraphs (A), (B), and (C) of paragraph (1);\n**(B)**\noffer programs and resources designed in consultation with and intended for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(C)**\noffer programs and resources in the communities in which the respective eligible entities are located that\u2014\n**(i)**\npromote maternal mental health and maternal substance use disorder treatments and supports that are aligned with evidence-based practices for improving maternal mental and behavioral health outcomes for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(ii)**\naddress social determinants of maternal health;\n**(iii)**\npromote evidence-based health literacy and pregnancy, childbirth, and parenting education;\n**(iv)**\nprovide support from perinatal health workers;\n**(v)**\nprovide culturally and linguistically congruent training to perinatal health workers;\n**(vi)**\nconduct or support research on maternal health issues disproportionately impacting individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes;\n**(vii)**\noffer group prenatal care or group postpartum care;\n**(viii)**\ncoordinate mutual aid efforts during infant formula shortages, including community milk depots, donor human milk banks and exchanges, and forums for community outreach and education;\n**(ix)**\nprovide support to individuals or family members of individuals who suffered a pregnancy loss, pregnancy-associated death, or pregnancy-related death; or\n**(x)**\noperate midwifery practices that provide culturally and linguistically congruent maternal health care and support, including for the purposes of\u2014\n**(I)**\nsupporting additional education, training, and certification programs, including support for distance learning;\n**(II)**\nproviding financial support to current and future midwives to address education costs, debts, and other needs;\n**(III)**\nclinical site investments;\n**(IV)**\nsupporting preceptor development trainings;\n**(V)**\nexpanding the midwifery practice; or\n**(VI)**\nrelated needs identified by the midwifery practice and described in the practice\u2019s application; and\n**(D)**\nhave developed other programs and resources that address community-specific needs for pregnant and postpartum individuals and are aligned with evidence-based practices for improving maternal health outcomes for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n##### (f) Technical assistance\nThe Secretary shall provide to grant recipients under this section technical assistance on\u2014\n**(1)**\ncapacity building to establish or expand programs to advance maternal health equity;\n**(2)**\nbest practices in data collection, measurement, evaluation, and reporting; and\n**(3)**\nplanning for sustaining programs to advance maternal health equity after the period of the grant.\n##### (g) Evaluation\nNot later than the end of fiscal year 2031, the Secretary shall submit to the Congress an evaluation of the grant program under this section that\u2014\n**(1)**\nassesses the effectiveness of outreach efforts during the application process in diversifying the pool of grant recipients;\n**(2)**\nmakes recommendations for future outreach efforts to diversify the pool of grant recipients for Department of Health and Human Services grant programs and funding opportunities related to maternal health;\n**(3)**\nassesses the effectiveness of programs funded by grants under this section in improving maternal health outcomes for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes, to the extent practicable; and\n**(4)**\nmakes recommendations for future Department of Health and Human Services grant programs and funding opportunities that deliver funding to community-based organizations that provide programs and resources that are aligned with evidence-based practices for improving maternal health outcomes for individuals from demographic groups with elevated rates of maternal mortality, severe maternal morbidity, maternal health disparities, or other adverse perinatal or childbirth outcomes.\n##### (h) Authorization of appropriations\nTo carry out this section, there is authorized to be appropriated $100,000,000 for each of fiscal years 2027 through 2031.\n#### 3. Respectful maternity care training for all employees in maternity care settings\nPart B of title VII of the Public Health Service Act ( 42 U.S.C. 293 et seq. ) is amended by adding at the end the following new section:\n742. Respectful maternity care training for all employees in maternity care settings (a) Grants The Secretary shall award grants for programs to reduce and prevent bias, racism, and discrimination in maternity care settings and to advance respectful, culturally and linguistically congruent, trauma-informed care. (b) Special consideration In awarding grants under subsection (a), the Secretary shall give special consideration to applications for programs that would\u2014 (1) apply to all maternity care providers and any employees who interact with pregnant and postpartum individuals in the provider setting, including front desk employees, sonographers, schedulers, health care professionals, hospital or health system administrators, security staff, and other employees; (2) emphasize periodic, as opposed to one-time, trainings for all birthing professionals and employees described in paragraph (1); (3) address implicit bias, racism, and cultural humility; (4) be delivered in ongoing education settings for providers maintaining their licenses, with a preference for trainings that provide continuing education units; (5) include trauma-informed care best practices and an emphasis on shared decision making between providers and patients; (6) include antiracism training and programs; (7) be delivered in undergraduate programs that funnel into health professions schools; (8) be delivered in settings that apply to providers of the special supplemental nutrition program for women, infants, and children under section 17 of the Child Nutrition Act of 1966; (9) integrate bias training in obstetric emergency simulation trainings or related trainings; (10) include training for emergency department employees and emergency medical technicians on recognizing warning signs for severe pregnancy-related complications; (11) offer training to all maternity care providers on the value of racially, ethnically, and professionally diverse maternity care teams to provide culturally and linguistically congruent care; or (12) be based on one or more programs designed by a historically Black college or university or other minority-serving institution. (c) Application To seek a grant under subsection (a), an entity shall submit an application at such time, in such manner, and containing such information as the Secretary may require. (d) Reporting Each recipient of a grant under this section shall annually submit to the Secretary a report on the status of activities conducted using the grant, including, as applicable, a description of the impact of training provided through the grant on patient outcomes and patient experience for pregnant and postpartum individuals from racial and ethnic minority groups and their families. (e) Best practices Based on the annual reports submitted pursuant to subsection (d), the Secretary\u2014 (1) shall produce an annual report on the findings resulting from programs funded through this section; (2) shall disseminate such report to all recipients of grants under this section and to the public; and (3) may include in such report findings on best practices for improving patient outcomes and patient experience for pregnant and postpartum individuals from racial and ethnic minority groups and their families in maternity care settings. (f) Definitions In this section: (1) The term postpartum means the 1-year period beginning on the last day of an individual\u2019s pregnancy. (2) The term culturally and linguistically congruent means in agreement with the preferred cultural values, beliefs, worldview, language, and practices of the health care consumer and other stakeholders. (3) The term racial and ethnic minority group has the meaning given such term in section 1707(g)(1). (g) Authorization of appropriations To carry out this section, there is authorized to be appropriated $5,000,000 for each of fiscal years 2027 through 2031. .\n#### 4. Study on reducing and preventing bias, racism, and discrimination in maternity care settings\n##### (a) In general\nThe Secretary of Health and Human Services shall seek to enter into an agreement, not later than 90 days after the date of enactment of this Act, with the National Academies of Sciences, Engineering, and Medicine (referred to in this section as the National Academies ) under which the National Academies agree to\u2014\n**(1)**\nconduct a study on the design and implementation of programs to reduce and prevent bias, racism, and discrimination in maternity care settings and to advance respectful, culturally and linguistically congruent, trauma-informed care; and\n**(2)**\nnot later than 24 months after the date of enactment of this Act\u2014\n**(A)**\ncomplete the study; and\n**(B)**\ntransmit a report on the results of the study to the Congress.\n##### (b) Possible topics\nThe agreement entered into pursuant to subsection (a) may provide for the study of any of the following:\n**(1)**\nThe development of a scorecard or other evaluation standards for programs designed to reduce and prevent bias, racism, and discrimination in maternity care settings to assess the effectiveness of such programs in improving patient outcomes and patient experience for pregnant and postpartum individuals from racial and ethnic minority groups and their families.\n**(2)**\nDetermination of the types and frequency of training to reduce and prevent bias, racism, and discrimination in maternity care settings that are demonstrated to improve patient outcomes or patient experience for pregnant and postpartum individuals from racial and ethnic minority groups and their families.\n#### 5. Respectful maternity care compliance program\n##### (a) In general\nThe Secretary of Health and Human Services (referred to in this section as the Secretary ) shall award grants to accredited hospitals, health systems, and other maternity care settings to establish as an integral part of quality implementation initiatives within one or more hospitals or other birth settings a respectful maternity care compliance program.\n##### (b) Program requirements\nA respectful maternity care compliance program funded through a grant under this section shall\u2014\n**(1)**\ninstitutionalize mechanisms to allow patients receiving maternity care services, the families of such patients, or perinatal health workers supporting such patients to report instances of racism or evidence of bias on the basis of race, ethnicity, or another protected class;\n**(2)**\ninstitutionalize response mechanisms through which representatives of the program can directly follow up with the patient, if possible, and the patient\u2019s family in a timely manner;\n**(3)**\nprepare and make publicly available a hospital- or health system-wide strategy to reduce bias on the basis of race, ethnicity, or another protected class in the delivery of maternity care that includes\u2014\n**(A)**\ninformation on the training programs to reduce and prevent bias, racism, and discrimination on the basis of race, ethnicity, or another protected class for all employees in maternity care settings;\n**(B)**\ninformation on the number of cases reported to the compliance program; and\n**(C)**\nthe development of methods to routinely assess the extent to which bias, racism, or discrimination on the basis of race, ethnicity, or another protected class is present in the delivery of maternity care to patients from racial and ethnic minority groups;\n**(4)**\ndevelop mechanisms to routinely collect and publicly report hospital-level data related to patient-reported experience of care; and\n**(5)**\nprovide annual reports to the Secretary with information about each case reported to the compliance program over the course of the year containing such information as the Secretary may require, such as\u2014\n**(A)**\ndeidentified demographic information on the patient in the case, such as race, ethnicity, gender identity, and primary language;\n**(B)**\nthe content of the report from the patient or the family of the patient to the compliance program;\n**(C)**\nthe response from the compliance program; and\n**(D)**\nto the extent applicable, institutional changes made as a result of the case.\n##### (c) Secretary requirements\n**(1) Processes**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish processes for\u2014\n**(A)**\ndisseminating best practices for establishing and implementing a respectful maternity care compliance program within a hospital or other birth setting;\n**(B)**\npromoting coordination and collaboration between hospitals, health systems, and other maternity care delivery settings on the establishment and implementation of respectful maternity care compliance programs; and\n**(C)**\nevaluating the effectiveness of respectful maternity care compliance programs on maternal health outcomes and patient and family experiences, especially for patients from racial and ethnic minority groups and their families.\n**(2) Study**\n**(A) In general**\nNot later than 2 years after the date of enactment of this Act, the Secretary shall, through a contract with an independent research organization, conduct a study on strategies to address\u2014\n**(i)**\nracism or bias on the basis of race, ethnicity, or another protected class in the delivery of maternity care services; and\n**(ii)**\nsuccessful implementation of respectful care initiatives.\n**(B) Components of study**\nThe study shall include the following:\n**(i)**\nAn assessment of the reports submitted to the Secretary from the respectful maternity care compliance programs pursuant to subsection (b)(5).\n**(ii)**\nBased on such assessment, recommendations for potential accountability mechanisms related to cases of racism or bias on the basis of race, ethnicity, or another protected class in the delivery of maternity care services at hospitals and other birth settings. Such recommendations shall take into consideration medical and nonmedical factors that contribute to adverse patient experiences and maternal health outcomes.\n**(C) Report**\nThe Secretary shall submit to the Congress and make publicly available a report on the results of the study under this paragraph.\n##### (d) Authorization of appropriations\nTo carry out this section, there are authorized to be appropriated such sums as may be necessary for fiscal years 2027 through 2032.\n#### 6. GAO report\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act and annually thereafter, the Comptroller General of the United States shall submit to the Congress and make publicly available a report on the establishment of respectful maternity care compliance programs within hospitals, health systems, and other maternity care settings.\n##### (b) Matters included\nThe report under subsection (a) shall include the following:\n**(1)**\nInformation regarding the extent to which hospitals, health systems, and other maternity care settings have elected to establish respectful maternity care compliance programs, including\u2014\n**(A)**\nwhich hospitals and other birth settings elect to establish compliance programs and when such programs are established;\n**(B)**\nto the extent practicable, impacts of the establishment of such programs on maternal health outcomes and patient and family experiences in the hospitals and other birth settings that have established such programs, especially for patients from racial and ethnic minority groups and their families;\n**(C)**\ninformation on geographic areas, and types of hospitals or other birth settings, where respectful maternity care compliance programs are not being established and information on factors contributing to decisions to not establish such programs; and\n**(D)**\nrecommendations for establishing respectful maternity care compliance programs in geographic areas, and types of hospitals or other birth settings, where such programs are not being established.\n**(2)**\nWhether the funding made available to carry out this section has been sufficient and, if applicable, recommendations for additional appropriations to carry out this section.\n**(3)**\nSuch other information as the Comptroller General determines appropriate.\n#### 7. Definitions\nIn this Act:\n**(1) Culturally and linguistically congruent**\nThe term culturally and linguistically congruent , with respect to care or maternity care, means care that is in agreement with the preferred cultural values, beliefs, worldview, language, and practices of the health care consumer and other stakeholders.\n**(2) Maternal mortality**\nThe term maternal mortality means a death occurring during or within a 1-year period after pregnancy, caused by pregnancy-related or childbirth complications, including a suicide, overdose, or other death resulting from a mental health or substance use disorder attributed to or aggravated by pregnancy-related or childbirth complications.\n**(3) Perinatal health worker**\nThe term perinatal health worker means a nonclinical health worker focused on maternal or perinatal health, such as a doula, community health worker, peer supporter, lactation educator or counselor, nutritionist or dietitian, childbirth educator, social worker, home visitor, patient navigator or coordinator, or language interpreter.\n**(4) Postpartum**\nThe term postpartum refers to the 1-year period beginning on the last day of the pregnancy of an individual.\n**(5) Pregnancy-associated death**\nThe term pregnancy-associated death means a death of a pregnant or postpartum individual, by any cause, that occurs during, or within 1 year following, the individual\u2019s pregnancy, regardless of the outcome, duration, or site of the pregnancy.\n**(6) Pregnancy-related death**\nThe term pregnancy-related death means a death of a pregnant or postpartum individual that occurs during, or within 1 year following, the individual\u2019s pregnancy, from a pregnancy complication, a chain of events initiated by pregnancy, or the aggravation of an unrelated condition by the physiologic effects of pregnancy.\n**(7) Racial and ethnic minority group**\nThe term racial and ethnic minority group has the meaning given such term in section 1707(g)(1) of the Public Health Service Act ( 42 U.S.C. 300u\u20136(g)(1) ).\n**(8) Severe maternal morbidity**\nThe term severe maternal morbidity means a health condition, including mental health conditions and substance use disorders, attributed to or aggravated by pregnancy or childbirth that results in significant short-term or long-term consequences to the health of the individual who was pregnant.\n**(9) Social determinants of maternal health**\nThe term social determinants of maternal health means nonclinical factors that impact maternal health outcomes.",
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
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-25",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4195",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Kira Johnson Act",
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
        "name": "Health",
        "updateDate": "2026-04-13T13:51:47Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8074ih.xml"
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
      "title": "Kira Johnson Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Kira Johnson Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To end preventable maternal mortality and severe maternal morbidity in the United States and close disparities in maternal health outcomes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:45Z"
    }
  ]
}
```
