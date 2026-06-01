# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2711
- Title: Invest to Protect Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2711
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-05-22T08:07:17Z
- Update date including text: 2026-05-22T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2711",
    "number": "2711",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Invest to Protect Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:17Z",
    "updateDateIncludingText": "2026-05-22T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:06:35Z",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "FL"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NV"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "RI"
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
      "sponsorshipDate": "2025-04-08",
      "state": "MI"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NM"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "IL"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "MN"
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
      "sponsorshipDate": "2025-04-08",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-08",
      "state": "ME"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "WA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NH"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "NJ"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NH"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "MO"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-12-26",
      "state": "PA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-12-30",
      "state": "NE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-12-30",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
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
      "sponsorshipDate": "2026-01-20",
      "state": "NY"
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
      "sponsorshipDate": "2026-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "IA"
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
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "HI"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "TN"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "WA"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-05-21",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2711ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2711\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Gottheimer (for himself, Mr. Rutherford , Mr. Horsford , Mr. Sorensen , Ms. Gillen , Mr. Costa , Mr. Panetta , Mr. Magaziner , Ms. Scholten , Mr. Garbarino , Mr. Vasquez , Mr. Ryan , Mr. Casten , Mr. Pallone , Ms. Craig , Mr. Deluzio , Mr. Harder of California , Mr. Carbajal , Ms. Lee of Nevada , Mr. Suozzi , Mr. Golden of Maine , Mr. Kennedy of New York , Ms. Budzinski , Mr. Correa , and Ms. Perez ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo establish a grant program to provide assistance to local law enforcement agencies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Invest to Protect Act of 2025 .\n#### 2. Grant program\n##### (a) Definitions\nIn this Act:\n**(1) De-escalation training**\nThe term de-escalation training means training relating to taking action or communicating verbally or non-verbally during a potential force encounter in an attempt to stabilize the situation and reduce the immediacy of the threat so that more time, options, and resources can be called upon to resolve the situation without the use of force or with a reduction in the force necessary.\n**(2) Director**\nThe term Director means the Director of the Office.\n**(3) Eligible local government**\nThe term eligible local government means\u2014\n**(A)**\na county, municipality, town, township, village, parish, borough, or other unit of general government below the State level that employs fewer than 175 law enforcement officers; and\n**(B)**\na Tribal government that employs fewer than 175 law enforcement officers.\n**(4) Law enforcement officer**\nThe term law enforcement officer has the meaning given the term career law enforcement officer in section 1709 of title I the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 ).\n**(5) Office**\nThe term Office means the Office of Community Oriented Policing Services of the Department of Justice.\n##### (b) Establishment\nThere is established within the Office a grant program to\u2014\n**(1)**\nprovide training and access to mental health resources to local law enforcement officers; and\n**(2)**\nimprove the recruitment and retention of local law enforcement officers.\n##### (c) Authority\nNot later than 120 days after the date of enactment of this Act, the Director shall award grants to eligible local governments as a part of the grant program established under subsection (b).\n##### (d) Applications\n**(1) Barriers**\nThe Attorney General shall determine what barriers exist to establishing a streamlined application process for grants under this section.\n**(2) Report**\n**(A) In general**\nNot later than 60 days after the date of enactment of this Act, the Attorney General shall submit to Congress a report that includes a plan to execute a streamlined application process for grants under this section under which an eligible local government seeking a grant under this section can reasonably complete the application in not more than 2 hours.\n**(B) Contents of plan**\nThe plan required under subparagraph (A) may include a plan for\u2014\n**(i)**\nproactively providing eligible local governments seeking a grant under this section with information on the data eligible local governments will need to prepare before beginning the grant application; and\n**(ii)**\nensuring technical assistance is available for eligible local governments seeking a grant under this section before and during the grant application process, including through dedicated liaisons within the Office.\n**(3) Applications**\nIn selecting eligible local governments to receive grants under this section, the Director shall use the streamlined application process described in paragraph (2)(A).\n##### (e) Eligible activities\nAn eligible local government that receives a grant under this section may use amounts from the grant only for\u2014\n**(1)**\nde-escalation training for law enforcement officers;\n**(2)**\nvictim-centered training for law enforcement officers in handling situations of domestic violence;\n**(3)**\nevidence-based law enforcement safety training for\u2014\n**(A)**\nactive shooter situations;\n**(B)**\nthe safe handling of illicit drugs and precursor chemicals;\n**(C)**\nrescue situations;\n**(D)**\nrecognizing and countering ambush attacks; or\n**(E)**\nresponse to calls for service involving\u2014\n**(i)**\npersons with mental health needs;\n**(ii)**\npersons with substance use disorders;\n**(iii)**\nveterans;\n**(iv)**\npersons with disabilities;\n**(v)**\nvulnerable youth;\n**(vi)**\npersons who are victims of domestic violence, sexual assault, or trafficking; or\n**(vii)**\npersons experiencing homelessness or living in poverty;\n**(4)**\nthe offsetting of overtime costs associated with scheduling issues relating to the participation of a law enforcement officer in the training described in paragraphs (1) through (3), (9), and (10);\n**(5)**\na signing bonus for a law enforcement officer in an amount determined by the eligible local government;\n**(6)**\na retention bonus for a law enforcement officer\u2014\n**(A)**\nin an amount determined by the eligible local government that does not exceed 20 percent of the salary of the law enforcement officer; and\n**(B)**\nwho\u2014\n**(i)**\nhas been employed at the law enforcement agency for not fewer than 5 years;\n**(ii)**\nhas not been found by an internal investigation to have engaged in serious misconduct; and\n**(iii)**\ncommits to remain employed by the law enforcement agency for not less than 3 years after the date of receipt of the bonus;\n**(7)**\na stipend for the graduate education of law enforcement officers in the area of mental health, public health, or social work, which shall not exceed the lesser of\u2014\n**(A)**\n$10,000; or\n**(B)**\nthe amount the law enforcement officer pays towards such graduate education;\n**(8)**\nproviding access to patient-centered behavioral health services for law enforcement officers, which may include resources for risk assessments, evidence-based, trauma-informed care to treat post-traumatic stress disorder or acute stress disorder, peer support and counselor services and family supports, and the promotion of improved access to high quality mental health care through telehealth;\n**(9)**\nthe implementation of evidence-based best practices and training on the use of lethal and nonlethal force;\n**(10)**\nthe implementation of evidence-based best practices and training on the duty of care and the duty to intervene; and\n**(11)**\ndata collection for police practices relating to officer and community safety.\n##### (f) Reporting requirements for grant recipients\n**(1) In general**\nThe Director shall establish reasonable reporting requirements specifically relating to a grant awarded under this section for eligible local governments that receive such a grant in order to assist with the evaluation by the Office of the program established under this section.\n**(2) Considerations**\nIn establishing requirements under paragraph (1), the Director shall consider the capacity of law enforcement agencies with fewer than 175 officers to collect and report information.\n##### (g) Disclosure of officer recruitment and retention bonuses\n**(1) In general**\nNot later than 60 days after the date on which an eligible local government that receives a grant under this section awards a signing or retention bonus described in paragraph (5) or (6) of subsection (e), the eligible local government shall disclose to the Director and make publicly available on a website of the eligible local government the amount of the bonus.\n**(2) Report**\nThe Attorney General shall submit to the appropriate congressional committees an annual report that includes each signing or retention bonus disclosed under paragraph (1) during the preceding year.\n##### (h) Grant accountability\n**(1) In general**\nAll grants awarded by the Director under this section shall be subject to the accountability provisions described in this subsection.\n**(2) Audit requirement**\n**(A) Definition**\nIn this paragraph, the term unresolved audit finding means a finding in the final audit report of the Inspector General of the Department of Justice that the audited grantee has used grant funds for an unauthorized expenditure or otherwise unallowable cost that is not closed or resolved within 12 months from the date when the final audit report is issued.\n**(B) Audits**\nBeginning in the first fiscal year beginning after the date of enactment of this subsection, and in each fiscal year thereafter, the Inspector General of the Department of Justice shall conduct audits of recipients of grants under this section to prevent waste, fraud, and abuse of funds by grantees. The Inspector General of the Department of Justice shall determine the appropriate number of grantees to be audited each year.\n**(C) Mandatory exclusion**\nA recipient of grant funds under this section that is found to have an unresolved audit finding shall not be eligible to receive grant funds under this section during the first 3 fiscal years beginning after the end of the 12-month period described in subparagraph (A).\n**(D) Reimbursement**\nIf an eligible local government is awarded grant funds under this section during the 3-fiscal-year period during which the eligible local government is barred from receiving grants under subparagraph (C), the Attorney General shall\u2014\n**(i)**\ndeposit an amount equal to the amount of the grant funds that were improperly awarded to the grantee into the General Fund of the Treasury; and\n**(ii)**\nseek to recoup the costs of the repayment to the fund from the grant recipient that was erroneously awarded grant funds.\n**(3) Annual certification**\nBeginning in the fiscal year during which audits commence under paragraph (2)(B), the Attorney General shall submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives an annual certification\u2014\n**(A)**\nindicating whether\u2014\n**(i)**\nall audits issued by the Office of the Inspector General of the Department of Justice under paragraph (2) have been completed and reviewed by the appropriate Assistant Attorney General or Director;\n**(ii)**\nall mandatory exclusions required under paragraph (2)(C) have been issued; and\n**(iii)**\nall reimbursements required under paragraph (2)(D) have been made; and\n**(B)**\nthat includes a list of any grant recipients excluded under paragraph (2) from the previous year.\n##### (i) Program evaluation\nNot less frequently than annually, the Attorney General shall analyze the information provided by eligible local governments pursuant to the reporting requirements established under subsection (f)(1) to evaluate the efficacy of programs funded by the grant program under this section.\n##### (j) Preventing duplicative grants\n**(1) In general**\nBefore the Director awards a grant to an eligible local government under this section, the Attorney General shall compare potential grant awards with other grants awarded by the Attorney General to determine if grant awards are or have been awarded for a similar purpose.\n**(2) Report**\nIf the Attorney General awards grants to the same applicant for a similar purpose, whether through the grant program under this section or another grant program administered by the Department of Justice, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes\u2014\n**(A)**\na list of all such grants awarded, including the total dollar amount of any such grants awarded; and\n**(B)**\nthe reason the Attorney General awarded multiple grants to the same applicant for a similar purpose.\n##### (k) Authorization of appropriations\nThere are authorized to be appropriated to carry out this section not more than $50,000,000 for each of fiscal years 2027 through 2031.",
      "versionDate": "2025-04-08",
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
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Invest to Protect Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-01T11:17:25Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2711ih.xml"
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
      "title": "Invest to Protect Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Invest to Protect Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to provide assistance to local law enforcement agencies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T05:18:39Z"
    }
  ]
}
```
