# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5886?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5886
- Title: Warrior Road Act
- Congress: 119
- Bill type: HR
- Bill number: 5886
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-01-07T09:05:51Z
- Update date including text: 2026-01-07T09:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-11-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5886",
    "number": "5886",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000622",
        "district": "1",
        "firstName": "Jimmy",
        "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
        "lastName": "Patronis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Warrior Road Act",
    "type": "HR",
    "updateDate": "2026-01-07T09:05:51Z",
    "updateDateIncludingText": "2026-01-07T09:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-01T17:04:03Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5886ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5886\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Patronis introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prioritize highway improvement projects that promote national defense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Warrior Road Act .\n#### 2. Civil defense\nSection 310 of title 23, United States Code, is amended by striking to consult, from time to time, with the Federal Civil Defense Administrator relative to the civil defense aspects of highways so constructed or reconstructed and inserting to develop a priority listing containing the 3 highest priority projects from each State relative to the civil defense aspects of highways so constructed or reconstructed. At least every 2 years, the Secretary shall consult with the Administrator of the Federal Emergency Management Agency to consider whether to update such listing or to reprioritize projects. The Secretary shall submit each listing, and any update carried out pursuant to this section, in an electronic format to each Member of Congress .\n#### 3. Report on highway improvement projects that promote national defense\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation, in consultation with the Secretary of War, shall submit to Congress, including in an electronic format to each Member of Congress, a report that contains a list of highway improvement projects that\u2014\n**(1)**\nwould promote national defense consistent with the core purposes of highway funding; and\n**(2)**\nare designated as important to national defense pursuant to section 210 of title 23, United States Code.\n##### (b) Highest priority projects in each State\nThe list compiled pursuant to subsection (a) shall include not less than 3 of the highest priority projects in each State.\n#### 4. Prioritizing funding for national defense\n##### (a) Discretionary grants\nIn awarding discretionary grants under title 23, United States Code, the Secretary of Transportation shall give priority to projects designated as important to national defense pursuant to section 210 of title 23, United States Code, and projects designated under section 311 of title 23, United States Code.\n##### (b) Apportionment funds\nTo be eligible for disbursement of funds under section 104 of title 23, United States Code, a State or metropolitan planning organization shall ensure that such State or organization will give priority to projects designated as important to national defense pursuant to section 210 of title 23, United States Code, and projects designated under section 311 of title 23, United States Code.\n#### 5. Definition of State\nThe term State has the meaning given the term in section 101 of title 23, United States Code.",
      "versionDate": "2025-10-31",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-11-19T14:22:59Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5886ih.xml"
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
      "title": "Warrior Road Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Warrior Road Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-07T12:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prioritize highway improvement projects that promote national defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-07T12:18:16Z"
    }
  ]
}
```
