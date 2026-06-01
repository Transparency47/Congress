# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/463
- Title: Condemning the illegal, international use of flag-of-convenience practices.
- Congress: 119
- Bill type: HRES
- Bill number: 463
- Origin chamber: House
- Introduced date: 2025-06-03
- Update date: 2025-07-22T12:31:17Z
- Update date including text: 2025-07-22T12:31:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in House
- 2025-06-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Sponsor introductory remarks on measure. (CR H2389)
- 2025-06-03 - IntroReferral: Submitted in House
- 2025-06-03 - IntroReferral: Submitted in House
- 2025-06-04 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.
- Latest action: 2025-06-03: Submitted in House

## Actions

- 2025-06-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-03 - IntroReferral: Sponsor introductory remarks on measure. (CR H2389)
- 2025-06-03 - IntroReferral: Submitted in House
- 2025-06-03 - IntroReferral: Submitted in House
- 2025-06-04 - Committee: Referred to the Subcommittee on Coast Guard and Maritime Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/463",
    "number": "463",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "Condemning the illegal, international use of flag-of-convenience practices.",
    "type": "HRES",
    "updateDate": "2025-07-22T12:31:17Z",
    "updateDateIncludingText": "2025-07-22T12:31:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2389)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-04T21:03:26Z",
              "name": "Referred to"
            }
          },
          "name": "Coast Guard and Maritime Transportation Subcommittee",
          "systemCode": "hspw07"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-03T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "HI"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "HI"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
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
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "AS"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "WA"
    },
    {
      "bioguideId": "K000404",
      "district": "0",
      "firstName": "Kimberlyn",
      "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "King-Hinds",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MP"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres463ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 463\nIN THE HOUSE OF REPRESENTATIVES\nJune 3, 2025 Mr. Moylan (for himself, Ms. Tokuda , Mr. Case , Mr. Huffman , Mr. Garamendi , and Mrs. Radewagen ) submitted the following resolution; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nCondemning the illegal, international use of flag-of-convenience practices.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the need for more funding, employment opportunities, and protections for the United States maritime industry;\n**(2)**\nsupports initiatives that seek to address critical shortfalls in the United States shipbuilding and ship repair industries while reiterating the need for a capable, reliable United States maritime auxiliary;\n**(3)**\nreaffirms the congressional support for United States businesses that rely on robust and reliable maritime shipping, shipbuilding, fishing, and tourism industries;\n**(4)**\ncondemns the international use of flag of convenience to avoid tariffs, sanctions, workplace rights, and basic safety standards, as well as supporting criminal opportunity, illegal, unreported, and unregulated fishing, and terrorist operations;\n**(5)**\nreiterates the mission of the United States Coast Guard and encourages further international maritime collaborations through vital shiprider agreements;\n**(6)**\nstrongly condemns countries that purposefully ignore maritime safety standards and mariners\u2019 workplace rights;\n**(7)**\nemphasizes the importance of Port State Control Agreement, including the Abuja Memorandum of Understanding, the Black Sea Memorandum of Understanding, the Caribbean Memorandum of Understanding, the Indian Ocean Memorandum of Understanding, the Mediterranean Memorandum of Understanding, the Paris Memorandum of Understanding, the Riyadh Memorandum of Understanding, the Tokyo Memorandum of Understanding, and the Vi\u00f1a del Mar Agreement;\n**(8)**\nstrongly supports the efforts of the International Transport Workers\u2019 Federation to prevent and mitigate the effects of flag-of-convenience practices; and\n**(9)**\ncalls on the United Nations, the International Maritime Organization, and the International Labour Organization to condemn flag-of-convenience practices globally and assist member nations in upholding global maritime standards.",
      "versionDate": "2025-06-03",
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
        "name": "International Affairs",
        "updateDate": "2025-07-22T12:31:17Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres463ih.xml"
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
      "title": "Condemning the illegal, international use of flag-of-convenience practices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T08:33:25Z"
    },
    {
      "title": "Condemning the illegal, international use of flag-of-convenience practices.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T08:05:37Z"
    }
  ]
}
```
