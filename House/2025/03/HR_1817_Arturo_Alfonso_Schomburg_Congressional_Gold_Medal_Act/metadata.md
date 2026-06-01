# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1817?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1817
- Title: Arturo Alfonso Schomburg Congressional Gold Medal Act
- Congress: 119
- Bill type: HR
- Bill number: 1817
- Origin chamber: House
- Introduced date: 2025-03-03
- Update date: 2025-03-19T15:15:08Z
- Update date including text: 2025-03-19T15:15:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-03: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-03: Introduced in House

## Actions

- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Introduced in House
- 2025-03-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-03",
    "latestAction": {
      "actionDate": "2025-03-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1817",
    "number": "1817",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Arturo Alfonso Schomburg Congressional Gold Medal Act",
    "type": "HR",
    "updateDate": "2025-03-19T15:15:08Z",
    "updateDateIncludingText": "2025-03-19T15:15:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on House Administration, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-03",
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
          "date": "2025-03-03T17:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-03T17:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "IN"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-03",
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
      "sponsorshipDate": "2025-03-03",
      "state": "NJ"
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
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-03",
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
      "sponsorshipDate": "2025-03-03",
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
      "sponsorshipDate": "2025-03-03",
      "state": "FL"
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
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1817ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1817\nIN THE HOUSE OF REPRESENTATIVES\nMarch 3, 2025 Ms. Vel\u00e1zquez (for herself, Mr. Soto , Mr. Torres of New York , Mr. Carson , Ms. Ocasio-Cortez , Mr. Jackson of Illinois , Mrs. McIver , Mr. Goldman of New York , Mr. Espaillat , Ms. Kelly of Illinois , Mrs. Cherfilus-McCormick , Ms. Wilson of Florida , and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on House Administration , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo award a Congressional Gold Medal to Arturo Alfonso Schomburg, in recognition of his pioneering work in collecting and preserving the history and culture of the African diaspora.\n#### 1. Short title\nThis Act may be cited as the Arturo Alfonso Schomburg Congressional Gold Medal Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nArturo Alfonso Schomburg was born on January 24, 1874, in Santurce, Puerto Rico, to a Puerto Rican father of German descent and an Afro-Caribbean mother from St. Croix.\n**(2)**\nIn his youth, a teacher told Schomburg that people of African descent had no history, heroes, or accomplishments, which inspired him to dedicate his life to proving this notion wrong by collecting evidence of the contributions of Africans and their descendants.\n**(3)**\nAt the age of 17, Schomburg immigrated to New York City, where he became an active member of the intellectual community during the Harlem Renaissance, contributing significantly to the promotion of African and African American culture and history.\n**(4)**\nSchomburg amassed a personal collection of over 10,000 items related to Black history and the African diaspora, which he made accessible to the public.\n**(5)**\nHis collection featured original newspapers published by Frederick Douglass, poems by Phillis Wheatley, letters from Toussaint Louverture, books and journals by Paul Cuffe, and music composed by Chevalier de Saint-Georges.\n**(6)**\nDuring the 1920s, Schomburg was an active member of the Negro Society for Historical Research and the American Negro Academy, writing on the history of the global African diaspora and Cuban poets of African descent.\n**(7)**\nIn 1926, the New York Public Library acquired Schomburg\u2019s collection, which became the foundation for the Schomburg Center for Research in Black Culture in Harlem, a world-renowned institution for the study of the global Black experience.\n**(8)**\nSchomburg\u2019s archive has grown to more than 10 million items.\n**(9)**\nSchomburg\u2019s efforts have inspired generations of scholars, writers, and artists to explore and celebrate the rich history and culture of the African diaspora.\n**(10)**\nThe Congressional Gold Medal would be an appropriate way to honor Schomburg\u2019s legacy and his role in laying the foundation for future scholarship and global recognition of Black contributions to society.\n#### 3. Congressional gold medal\n##### (a) Award authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the posthumous presentation, on behalf of Congress, of a gold medal of appropriate design to Arturo Alfonso Schomburg, in recognition of his pioneering work in collecting and preserving the history and culture of the African diaspora.\n##### (b) Design and striking\nFor the purposes of the presentation referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary.\n##### (c) Smithsonian institution\n**(1) In general**\nFollowing the award of the gold medal under subsection (a), the gold medal shall be given to the National Museum of African American History and Culture of the Smithsonian Institution, where it shall be displayed as appropriate and made available for research.\n**(2) Sense of congress**\nIt is the sense of Congress that the Smithsonian Institution should make the gold medal received under paragraph (1) available for display elsewhere, particularly at other locations and events associated with Arturo Alfonso Schomburg.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck pursuant to section 3, at a price sufficient to cover the cost thereof, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medals\nThe medals struck pursuant to this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nor purposes of sections 5134 and 5136 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority To use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-03-03",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-03-19T15:15:07Z"
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
      "date": "2025-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1817ih.xml"
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
      "title": "Arturo Alfonso Schomburg Congressional Gold Medal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Arturo Alfonso Schomburg Congressional Gold Medal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To award a Congressional Gold Medal to Arturo Alfonso Schomburg, in recognition of his pioneering work in collecting and preserving the history and culture of the African diaspora.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T05:48:31Z"
    }
  ]
}
```
