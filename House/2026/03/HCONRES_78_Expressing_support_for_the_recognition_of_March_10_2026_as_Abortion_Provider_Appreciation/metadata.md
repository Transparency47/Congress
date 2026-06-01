# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/78?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/78
- Title: Expressing support for the recognition of March 10, 2026, as "Abortion Provider Appreciation Day".
- Congress: 119
- Bill type: HCONRES
- Bill number: 78
- Origin chamber: House
- Introduced date: 2026-03-12
- Update date: 2026-03-16T12:17:00Z
- Update date including text: 2026-03-16T12:17:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in House
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House
- Latest action: 2026-03-12: Submitted in House

## Actions

- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-12 - IntroReferral: Submitted in House
- 2026-03-12 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/78",
    "number": "78",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Expressing support for the recognition of March 10, 2026, as \"Abortion Provider Appreciation Day\".",
    "type": "HCONRES",
    "updateDate": "2026-03-16T12:17:00Z",
    "updateDateIncludingText": "2026-03-16T12:17:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T13:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-12T13:31:20Z",
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
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MN"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CO"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "WI"
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
      "sponsorshipDate": "2026-03-12",
      "state": "DC"
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
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-12",
      "state": "HI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MA"
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
      "sponsorshipDate": "2026-03-12",
      "state": "GA"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-12",
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
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
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
      "sponsorshipDate": "2026-03-12",
      "state": "NC"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
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
      "sponsorshipDate": "2026-03-12",
      "state": "CT"
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
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
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
      "sponsorshipDate": "2026-03-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres78ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 78\nIN THE HOUSE OF REPRESENTATIVES\nMarch 12, 2026 Ms. Pressley (for herself, Ms. Omar , Ms. DeGette , Mr. Swalwell , Ms. Moore of Wisconsin , Ms. Norton , Mrs. Ramirez , Ms. Salinas , Mr. Doggett , Ms. Tokuda , Mrs. Watson Coleman , Mr. Moulton , Mr. Johnson of Georgia , Ms. Crockett , Ms. Wilson of Florida , Mr. Garc\u00eda of Illinois , Ms. Ross , Ms. Johnson of Texas , Mr. Larson of Connecticut , Ms. Schakowsky , Ms. Bonamici , Ms. Chu , and Ms. Simon ) submitted the following concurrent resolution; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nCONCURRENT RESOLUTION\nExpressing support for the recognition of March 10, 2026, as Abortion Provider Appreciation Day .\nThat Congress\u2014\n**(1)**\nrecognizes Abortion Provider Appreciation Day to celebrate the courage, compassion, and high-quality care that abortion providers and staff offer to patients and their families across the United States;\n**(2)**\nlauds communities across the United States who are proud to be home to abortion providers and staff;\n**(3)**\naffirms the commitment of Congress to ensuring the safety of abortion providers, the ability of abortion providers to continue providing the essential care their patients need, and the right of patients to access abortion care no matter where they live, free from fear of violence, criminalization, or stigma;\n**(4)**\ncondemns the decisions of the Supreme Court of the United States, as well as the actions of the current administration and antiabortion extremists, to limit and stigmatize abortion care, which has had a devastating impact on abortion providers and the communities they care for, threatening the work and livelihoods of providers and staff, and worsening the strain on providers who work in States where abortion is still available; and\n**(5)**\ndeclares a vision for a future free from all abortion restrictions and bans, where everyone has full access to the care they need without fear of penalty or stigma, and affirms the commitment of Congress to working toward that goal in partnership with providers, patients, advocates, and their communities.",
      "versionDate": "2026-03-12",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "18",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the recognition of March 10, 2025, as \"Abortion Provider Appreciation Day\".",
      "type": "HCONRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-10",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S1633-1634)"
      },
      "number": "9",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A concurrent resolution expressing support for the recognition of March 10, 2025, as \"Abortion Provider Appreciation Day\".",
      "type": "SCONRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-10",
        "text": "Referred to the Committee on Health, Education, Labor, and Pensions. (text: CR S966)"
      },
      "number": "28",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A concurrent resolution expressing support for the recognition of March 10, 2026, as \"Abortion Provider Appreciation Day\".",
      "type": "SCONRES"
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
        "updateDate": "2026-03-16T12:17:00Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres78ih.xml"
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
      "title": "Expressing support for the recognition of March 10, 2026, as \"Abortion Provider Appreciation Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T08:19:24Z"
    },
    {
      "title": "Expressing support for the recognition of March 10, 2026, as \"Abortion Provider Appreciation Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T08:05:22Z"
    }
  ]
}
```
