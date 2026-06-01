# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3289
- Title: Crime Gun Tracing Modernization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3289
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-01-10T07:01:27Z
- Update date including text: 2026-01-10T07:01:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3289",
    "number": "3289",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Crime Gun Tracing Modernization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T07:01:27Z",
    "updateDateIncludingText": "2026-01-10T07:01:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T23:27:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3289is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3289\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Whitehouse (for himself and Mr. Merkley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 923 of title 18, United States Code, to require an electronic, searchable database of the importation, production, shipment, receipt, sale, or other disposition of firearms.\n#### 1. Short title\nThis Act may be cited as the Crime Gun Tracing Modernization Act of 2025 .\n#### 2. Electronic, searchable databases\nSection 923(g) of title 18, United States Code, is amended by adding at the end the following:\n(8) (A) In this paragraph, the term foreign intelligence information has the meaning given the term in section 101 of the Foreign Intelligence Surveillance Act of 1978 ( 50 U.S.C. 1801 ). (B) Not later than 3 years after the date of enactment of this paragraph, the National Tracing Center of the Bureau of Alcohol, Tobacco, Firearms and Explosives (referred to in this paragraph as the National Tracing Center ) shall establish and maintain electronic, searchable databases of all records within its possession of the importation, production, shipment, receipt, sale, or other disposition of firearms required to be submitted to the Bureau of Alcohol, Tobacco, Firearms and Explosives by persons licensed under this chapter. (C) Each licensee under this chapter may provide the National Tracing Center with electronic access, consistent with the requirements of this paragraph, to all records within the licensee\u2019s possession that are required to be kept under this chapter. (D) A licensee may voluntarily relinquish possession of any non-electronic record required to be kept under this chapter to the Bureau of Alcohol, Tobacco, Firearms and Explosives if\u2014 (i) 10 years have elapsed from the date of the firearm transaction; or (ii) in the case of paper acquisition and disposition books, 10 years have elapsed without any open disposition entries and with no dispositions recorded in the record. (E) The National Tracing Center\u2014 (i) shall have remote access to and may query, search, or otherwise access the electronic databases described in this paragraph; and (ii) may, with the permission of a State, or political subdivision of a State, have remote access to, and may query, search, or otherwise access the databases of the firearms registration system or pawnbroker records system of the State or political subdivision. (F) The National Tracing Center may query, search, or otherwise access the electronic databases described in this paragraph for only the following purposes: (i) To obtain information related to a bona fide law enforcement investigation by a Federal, State, local, Tribal, or foreign law enforcement agency. (ii) To obtain information that is\u2014 (I) foreign intelligence information; or (II) necessary to understand, or to assess the importance of, foreign intelligence information. (iii) To obtain information necessary during a compliance inspection of an active licensee who has submitted non-electronic records in accordance with subparagraph (D). (G) The databases established under this paragraph\u2014 (i) shall be electronically searchable by date of acquisition or disposition, license number, and the information identified on each firearm or other firearm descriptor, including the manufacturer, importer, model, serial number, type, and caliber or gauge; (ii) shall not be electronically searchable by the personally identifiable information of any individual; and (iii) shall include in search results the entire contents of the relevant records kept by the licensee. (H) This paragraph shall take effect notwithstanding any other provision of law, including any temporary or permanent restrictions placed on funds made available to the Bureau of Alcohol, Tobacco, Firearms and Explosives, or the Department of Justice. (I) Not later than 1 year after the date of enactment of this paragraph, and every 2 years thereafter, the Comptroller General of the United States shall\u2014 (i) carry out an audit on compliance by the National Tracing Center and the Bureau of Alcohol, Tobacco, Firearms and Explosives with the requirements of this paragraph; and (ii) submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on the audit carried out under clause (i). .",
      "versionDate": "2025-12-01",
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
        "actionDate": "2025-11-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "6223",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Crime Gun Tracing Modernization Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-18T17:08:26Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3289is.xml"
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
      "title": "Crime Gun Tracing Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Crime Gun Tracing Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 923 of title 18, United States Code, to require an electronic, searchable database of the importation, production, shipment, receipt, sale, or other disposition of firearms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:32Z"
    }
  ]
}
```
