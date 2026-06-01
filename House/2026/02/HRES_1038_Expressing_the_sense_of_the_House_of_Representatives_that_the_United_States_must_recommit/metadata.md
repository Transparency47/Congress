# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1038?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1038
- Title: Expressing the sense of the House of Representatives that the United States must recommit to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment to the United States Constitution to ensure that our democracy works for all of us, not just a powerful few.
- Congress: 119
- Bill type: HRES
- Bill number: 1038
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-02-12T14:59:04Z
- Update date including text: 2026-02-12T14:59:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House
- Latest action: 2026-02-04: Submitted in House

## Actions

- 2026-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Submitted in House
- 2026-02-04 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1038",
    "number": "1038",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "T000481",
        "district": "12",
        "firstName": "Rashida",
        "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
        "lastName": "Tlaib",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Expressing the sense of the House of Representatives that the United States must recommit to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment to the United States Constitution to ensure that our democracy works for all of us, not just a powerful few.",
    "type": "HRES",
    "updateDate": "2026-02-12T14:59:04Z",
    "updateDateIncludingText": "2026-02-12T14:59:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-02-04T15:01:15Z",
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
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MN"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sponsorshipDate": "2026-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sponsorshipDate": "2026-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MN"
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
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "MA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1038ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1038\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Tlaib (for herself, Mr. Costa , Ms. Craig , Mr. Evans of Pennsylvania , Ms. Lee of Pennsylvania , Mr. Lynch , Mr. Moulton , Ms. Omar , Mrs. Ramirez , Ms. Stansbury , Ms. Pressley , and Mr. Cisneros ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nExpressing the sense of the House of Representatives that the United States must recommit to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment to the United States Constitution to ensure that our democracy works for all of us, not just a powerful few.\nThat it is the sense of the House of Representatives that\u2014\n**(1)**\nCongress affirm the Fourteenth Amendment as a cornerstone of American multiracial democracy and a guarantor of birthright citizenship, due process, and equal protection under the law;\n**(2)**\nevery branch of the Federal Government must act to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment;\n**(3)**\nCongress must reject and oppose any legislation, executive action, or policy that seeks to dismantle, weaken, or circumvent the guarantees of birthright citizenship, due process, or equal protection;\n**(4)**\nCongress must preserve and protect birthright citizenship for everyone born in the United States, as guaranteed by the Constitution;\n**(5)**\nCongress pledges to work toward the full realization of equal protection and due process for all;\n**(6)**\nCongress stands with individuals, communities, organized workers, and civic groups working to ensure that American democracy works for all people and not solely for the benefit of a powerful, wealthy few; and\n**(7)**\nCongress calls upon elected officials at every level of government to honor their constitutional obligations and to actively defend the principles embodied in the Fourteenth Amendment.",
      "versionDate": "2026-02-04",
      "versionType": "IH"
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2026-02-12T14:59:04Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1038ih.xml"
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
      "title": "Expressing the sense of the House of Representatives that the United States must recommit to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment to the United States Constitution to ensure that our democracy works for all of us, not just a powerful few.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T09:18:34Z"
    },
    {
      "title": "Expressing the sense of the House of Representatives that the United States must recommit to defend and uphold the rights and protections guaranteed by the Fourteenth Amendment to the United States Constitution to ensure that our democracy works for all of us, not just a powerful few.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T09:06:27Z"
    }
  ]
}
```
