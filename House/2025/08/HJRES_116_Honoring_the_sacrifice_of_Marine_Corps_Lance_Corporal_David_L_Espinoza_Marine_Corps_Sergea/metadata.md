# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/116
- Title: Honoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.
- Congress: 119
- Bill type: HJRES
- Bill number: 116
- Origin chamber: House
- Introduced date: 2025-08-26
- Update date: 2025-12-05T22:57:32Z
- Update date including text: 2025-12-05T22:57:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-26: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-08-26: Introduced in House

## Actions

- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Introduced in House
- 2025-08-26 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-26",
    "latestAction": {
      "actionDate": "2025-08-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/116",
    "number": "116",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001222",
        "district": "7",
        "firstName": "Max",
        "fullName": "Rep. Miller, Max L. [R-OH-7]",
        "lastName": "Miller",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Honoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.",
    "type": "HJRES",
    "updateDate": "2025-12-05T22:57:32Z",
    "updateDateIncludingText": "2025-12-05T22:57:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-26",
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
      "actionDate": "2025-08-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-26",
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
          "date": "2025-08-26T15:00:20Z",
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
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "MI"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "MI"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TN"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "AZ"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "FL"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "NY"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "FL"
    },
    {
      "bioguideId": "L000603",
      "district": "8",
      "firstName": "Morgan",
      "fullName": "Rep. Luttrell, Morgan [R-TX-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Luttrell",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "GA"
    },
    {
      "bioguideId": "M001216",
      "district": "7",
      "firstName": "Cory",
      "fullName": "Rep. Mills, Cory [R-FL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mills",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "SC"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "KY"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "TX"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "OH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "VA"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "IN"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "MI"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "TX"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "IN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres116ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 116\nIN THE HOUSE OF REPRESENTATIVES\nAugust 26, 2025 Mr. Miller of Ohio (for himself, Mr. Barrett , Mr. Bergman , Mr. Burchett , Mr. Ciscomani , Mr. Fine , Mr. Issa , Mr. Kean , Mr. Lawler , Mrs. Luna , Mr. Luttrell , Mr. McCormick , and Mr. Mills ) submitted the following joint resolution; which was referred to the Committee on Armed Services\nJOINT RESOLUTION\nHonoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.\nThat the United States of America\u2014\n**(1)**\ndesignates a National Day of Remembrance in honor of the American servicemembers who made the ultimate sacrifice at the bombing of Abbey Gate at the Hamid Karzai International Airport in Kabul, Afghanistan, on August 26, 2021;\n**(2)**\nexpresses its deepest condolences and gratitude to the Gold Star Families of those lost at Abbey Gate; and\n**(3)**\nremembers their honorable and faithful service to their Nation.",
      "versionDate": "2025-08-26",
      "versionType": "IH"
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
        "actionDate": "2025-09-17",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "79",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution honoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.",
      "type": "SJRES"
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
        "updateDate": "2025-09-19T18:49:26Z"
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
      "date": "2025-08-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres116ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-27T08:18:19Z"
    },
    {
      "title": "Honoring the sacrifice of Marine Corps Lance Corporal David L. Espinoza, Marine Corps Sergeant Nicole L. Gee, Marine Corps Staff Sergeant Darin Taylor Hoover, Army Staff Sergeant Ryan Christian Knauss, Marine Corps Corporal Hunter Lopez, Marine Corps Lance Corporal Rylee J. McCollum, Marine Corps Lance Corporal Dylan R. Merola, Marine Corps Lance Corporal Kareem M. Nikoui, Marine Corps Corporal Daegan W. Page, Marine Corps Sergeant Johanny Rosario, Marine Corps Corporal Humberto A. Sanchez, Marine Corps Lance Corporal Jared M. Schmitz, and Navy Petty Officer Third Class Maxton W. Soviak.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-27T08:05:26Z"
    }
  ]
}
```
