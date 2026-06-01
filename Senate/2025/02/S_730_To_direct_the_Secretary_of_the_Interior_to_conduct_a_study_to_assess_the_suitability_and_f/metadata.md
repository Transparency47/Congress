# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/730?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/730
- Title: African Burial Ground International Memorial Museum and Educational Center Study Act
- Congress: 119
- Bill type: S
- Bill number: 730
- Origin chamber: Senate
- Introduced date: 2025-02-25
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-25: Introduced in Senate
- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-02-25: Introduced in Senate

## Actions

- 2025-02-25 - IntroReferral: Introduced in Senate
- 2025-02-25 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-25",
    "latestAction": {
      "actionDate": "2025-02-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/730",
    "number": "730",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "African Burial Ground International Memorial Museum and Educational Center Study Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-25",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-25T22:35:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:12:47Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s730is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 730\nIN THE SENATE OF THE UNITED STATES\nFebruary 25, 2025 Mrs. Gillibrand introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo direct the Secretary of the Interior to conduct a study to assess the suitability and feasibility of establishing the African Burial Ground International Memorial Museum and Educational Center at the African Burial Ground National Monument, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the African Burial Ground International Memorial Museum and Educational Center Study Act .\n#### 2. Definitions\nIn this Act:\n**(1) Museum**\nThe term Museum means the African Burial Ground International Memorial Museum and Educational Center.\n**(2) National Monument**\nThe term National Monument means the African Burial Ground National Monument in the city of New York, New York.\n**(3) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the National Park Service.\n**(4) State**\nThe term State means the State of New York.\n#### 3. African Burial Ground International Memorial Museum and Educational Center study\n##### (a) Study\n**(1) In general**\nThe Secretary, in consultation with State and local historic preservation officers, State and local historical societies, State and local tourism offices, and other appropriate organizations and government agencies, shall conduct a study to assess the suitability and feasibility of establishing a museum and educational center at the National Monument, to be known as the African Burial Ground International Memorial Museum and Educational Center \u2014\n**(A)**\nto serve as a permanent living memorial and special tribute\u2014\n**(i)**\nto the enslaved who are buried at the African Burial Ground; and\n**(ii)**\nto other Africans who were enslaved in the United States and other parts of the world;\n**(B)**\nto reflect on the significance of the African Burial Ground;\n**(C)**\nto examine the African cultural traditions brought to the United States by the enslaved;\n**(D)**\nto explore in-depth the institution of slavery in the United States and other parts of the world;\n**(E)**\nto provide a space for\u2014\n**(i)**\npermanent and temporary exhibits; and\n**(ii)**\nthe collection and study of artifacts and documents;\n**(F)**\nto encourage collaboration between the Museum and the National Museum of African American History and Culture, other museums, historically Black colleges and universities, historical societies, educational institutions, and other appropriate entities and organizations, such as the African Burial Ground Memorial Foundation, including collaboration with respect to\u2014\n**(i)**\nthe development of cooperative programs and exhibitions, including through digital, electronic, and interactive technologies;\n**(ii)**\nthe identification, management, and care of Museum collections; and\n**(iii)**\nthe training of Museum and National Park Service professionals and other persons concerned with heritage preservation; and\n**(G)**\nin addition to any collaboration encouraged under subparagraph (F), to be associated with the National Museum of African American History and Culture, in a manner to be determined by the Secretary, in consultation with the Board of Regents of the Smithsonian Institution.\n**(2) Requirements**\nThe study conducted under paragraph (1) shall include analysis, documentation, and determinations regarding whether\u2014\n**(A)**\nthere is an assemblage of collections to be acquired and housed in the Museum that\u2014\n**(i)**\nrepresent distinctive aspects of African cultural traditions brought to the United States by the enslaved;\n**(ii)**\nare worthy of recognition, conservation, and interpretation;\n**(iii)**\nare important to any identified themes of the Museum;\n**(iv)**\ninclude DNA samples of well-preserved human remains that would enable researchers to trace home roots in Africa of those individuals buried at the African Burial Ground; and\n**(v)**\nare unlike any other anthropological collection in other symbolic sites;\n**(B)**\nthe Museum provides outstanding opportunities\u2014\n**(i)**\nto understand how the international slave trade contributed to the African diaspora;\n**(ii)**\nto explore in-depth the institution of slavery, as practiced in other parts of the world and in urban, rural, northern, and southern parts of the United States; and\n**(iii)**\nto help the people of the United States understand the past and honor the history of all people in the United States;\n**(C)**\nresidents, business interests, State and local governments, and nonprofit organizations, such as the African Burial Ground Memorial Foundation\u2014\n**(i)**\nare involved in the planning of the Museum;\n**(ii)**\nhave developed a conceptual financial plan that outlines the roles of all participants in the Museum, including the Federal Government; and\n**(iii)**\nhave demonstrated support for the designation of the Museum;\n**(D)**\nthe Secretary of the Interior, the Administrator of the General Services Administration, or other potential management entities would be best suited to operate the Museum; and\n**(E)**\nthe public supports the proposed location for the Museum at\u2014\n**(i)**\n22 Reade Street, which is adjacent to the National Monument; or\n**(ii)**\nany area within the National Monument other than the area described in clause (i).\n##### (b) Report\nNot later than 3 years after the date on which funds are first made available to carry out this Act, the Secretary shall submit to the Committee on Energy and Natural Resources of the Senate and the Committee on Natural Resources of the House of Representatives a report that describes\u2014\n**(1)**\nthe results of the study under subsection (a), including a description of\u2014\n**(A)**\nthe availability and cost of collections to be acquired and housed in the Museum;\n**(B)**\ncriteria for evaluating possible locations for the Museum in the State; and\n**(C)**\nthe costs of acquiring property for, constructing, operating, and maintaining the Museum; and\n**(2)**\nany conclusions and recommendations of the Secretary.",
      "versionDate": "2025-02-25",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-25",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "1567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "African Burial Ground International Memorial Museum and Educational Center Study Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cemeteries and funerals",
            "updateDate": "2025-12-15T20:56:32Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-15T20:57:08Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-12-15T20:56:11Z"
          },
          {
            "name": "Historic sites and heritage areas",
            "updateDate": "2025-12-15T20:56:43Z"
          },
          {
            "name": "Historical and cultural resources",
            "updateDate": "2025-12-15T20:56:57Z"
          },
          {
            "name": "Museums, exhibitions, cultural centers",
            "updateDate": "2025-12-15T20:56:16Z"
          },
          {
            "name": "New York City",
            "updateDate": "2025-12-15T20:56:21Z"
          },
          {
            "name": "New York State",
            "updateDate": "2025-12-15T20:56:27Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-12-15T20:56:49Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-12-15T20:57:02Z"
          },
          {
            "name": "World history",
            "updateDate": "2025-12-15T20:56:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-09T21:16:47Z"
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
      "date": "2025-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s730is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "African Burial Ground International Memorial Museum and Educational Center Study Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "African Burial Ground International Memorial Museum and Educational Center Study Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of the Interior to conduct a study to assess the suitability and feasibility of establishing the African Burial Ground International Memorial Museum and Educational Center at the African Burial Ground National Monument, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:21Z"
    }
  ]
}
```
