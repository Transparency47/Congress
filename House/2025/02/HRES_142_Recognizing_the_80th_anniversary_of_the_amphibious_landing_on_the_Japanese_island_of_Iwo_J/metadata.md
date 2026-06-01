# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/142
- Title: Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.
- Congress: 119
- Bill type: HRES
- Bill number: 142
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2025-07-03T20:04:13Z
- Update date including text: 2025-07-03T20:04:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - Committee: Submitted in House
- Latest action: 2025-02-18: Submitted in House

## Actions

- 2025-02-18 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-18 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/142",
    "number": "142",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C000059",
        "district": "41",
        "firstName": "Ken",
        "fullName": "Rep. Calvert, Ken [R-CA-41]",
        "lastName": "Calvert",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
    "type": "HRES",
    "updateDate": "2025-07-03T20:04:13Z",
    "updateDateIncludingText": "2025-07-03T20:04:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-18T18:05:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-18T18:05:25Z",
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
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "CA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "CA"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres142ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 142\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Calvert (for himself, Mr. Carbajal , and Mr. Issa ) submitted the following resolution; which was referred to the Committee on Armed Services , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nRecognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima that began on February 19, 1945, and ended on March 26, 1945;\n**(2)**\ncommemorates the iconic and historic raisings of the flag of the United States on Mount Suribachi that occurred on February 23, 1945;\n**(3)**\nhonors the marines, sailors, soldiers, army air crew, and coast guardsmen who fought bravely on Iwo Jima, including the thousands of Japanese soldiers who defended the island;\n**(4)**\nremembers and venerates the servicemembers who gave their last full measure of devotion on the battlefield;\n**(5)**\nrecognizes the Allied victory in the Battle of Iwo Jima, which\u2014\n**(A)**\nwas led by the United States Marine Corps; and\n**(B)**\nmade the defeat of the Empire of Japan in World War II possible;\n**(6)**\naffirms the immortal words of Admiral Chester Nimitz, who state that uncommon valor was a common virtue among the servicemembers of the United States who fought on Iwo Jima;\n**(7)**\nreaffirms the bonds of friendship between the United States and Japan;\n**(8)**\nencourages the people of the United States to honor the veterans of the Battle of Iwo Jima with appropriate programs, ceremonies and activities; and\n**(9)**\nhonors the service and sacrifice of the men and women who serve the United States today carrying on the proud tradition of the individuals who came before them.",
      "versionDate": "2025-02-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2025-02-20T15:58:24Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-02-20T15:58:24Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-02-20T15:58:24Z"
          },
          {
            "name": "Military history",
            "updateDate": "2025-02-20T15:58:24Z"
          },
          {
            "name": "National symbols",
            "updateDate": "2025-02-20T15:58:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:27:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hres142",
          "measure-number": "142",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-18",
          "originChamber": "HOUSE",
          "update-date": "2025-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres142v00",
            "update-date": "2025-03-31"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945.</p>"
        },
        "title": "Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres142.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hres142"
    },
    "title": "Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi."
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the 80th anniversary of the amphibious landing of U.S. troops\u00a0on the Japanese island of Iwo Jima in 1945 and commemorates the historic raising of the U.S.\u00a0flag on Mount Suribachi that occurred on February 23, 1945.</p>",
      "updateDate": "2025-03-31",
      "versionCode": "id119hres142"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres142ih.xml"
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
      "title": "Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T09:18:16Z"
    },
    {
      "title": "Recognizing the 80th anniversary of the amphibious landing on the Japanese island of Iwo Jima during World War II and the raisings of the flag of the United States on Mount Suribachi.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T09:05:16Z"
    }
  ]
}
```
