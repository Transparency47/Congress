# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7371
- Title: No Flight, No Fight Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7371
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-15T08:07:48Z
- Update date including text: 2026-05-15T08:07:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7371",
    "number": "7371",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "N000026",
        "district": "22",
        "firstName": "Troy",
        "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
        "lastName": "Nehls",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "No Flight, No Fight Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:48Z",
    "updateDateIncludingText": "2026-05-15T08:07:48Z"
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NV"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "G000589",
      "district": "5",
      "firstName": "Lance",
      "fullName": "Rep. Gooden, Lance [R-TX-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gooden",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "OR"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2026-02-17",
      "state": "NH"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NJ"
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
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "FL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "False",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7371ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7371\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Nehls (for himself, Ms. Titus , Mr. Van Drew , Mr. Carter of Louisiana , Mr. Fitzpatrick , Mr. Smith of New Jersey , Mr. Buchanan , Mr. Gooden , Mrs. Luna , Mr. Ciscomani , Ms. Lofgren , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo restrict the air transportation of certain live animals in interstate and foreign commerce to enhance aviation safety, biosecurity, and operational efficiency in civil aviation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Flight, No Fight Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nCivil aviation, including the carriage of cargo by air, is critical to the national transportation system and economy of the United States.\n**(2)**\nThe transportation of certain live animals by air, particularly adult roosters, presents unique challenges to aviation safety, biosecurity, and airline operational efficiency, including risks of stress-induced behavior, potential disease transmission, and disruptions during flight.\n**(3)**\nRapid air transport of adult roosters has been associated with facilitating illegal activities, such as cockfighting, which poses additional biosecurity risks through unregulated movement of birds that may carry avian diseases.\n**(4)**\nRestricting non-essential air shipments of adult roosters, while preserving exemptions for large-scale commercial poultry operations, will promote safer and more efficient air cargo operations without disrupting legitimate agricultural supply chains in the commercial egg and meat industries.\n**(5)**\nThe Federal Aviation Administration and the Department of Transportation have authority over the safety and regulation of civil aviation, including the carriage of cargo by aircraft.\n#### 3. Restriction on air transportation of adult roosters\n##### (a) In general\nChapter 449 of title 49, United States Code, is amended by adding at the end the following new section:\n#### 4. Restriction on air transportation of adult roosters\n##### (a) Prohibition\nExcept as provided in subsection (b), no air carrier or other person operating an aircraft in interstate or foreign air transportation shall knowingly transport an adult rooster as cargo.\n##### (b) Exemption for commercial farms\nThe prohibition under subsection (a) shall not apply if\u2014\n**(1)**\nthe transport of the adult rooster(s) originates from or is destined for a commercial farm; and\n**(2)**\nthe transport is conducted for legitimate agricultural purposes.\n##### (c) Certification\nAny person claiming an exemption under subsection (b) shall provide documentation certifying that the originating or destination farm qualifies as a commercial farm, including financial records or attestations consistent with guidelines of the Economic Research Service of the United States Department of Agriculture to the air carrier prior to the transport of the adult rooster(s). No air carrier may accept an adult rooster for transport without certification.\n##### (d) Definitions\nIn this section:\n**(1) Adult rooster**\nThe term adult rooster means a male chicken (Gallus gallus domesticus) that has reached sexual maturity, typically characterized by the development of spurs, a large comb, and crowing behavior, and is at least 6 months of age.\n**(2) Air carrier**\nThe term air carrier has the meaning given such term in section 40102.\n**(3) Commercial farm**\nThe term commercial farm means any farm with $350,000 or more in annual gross cash farm income (including sales of crops and livestock, government payments, and other farm-related income), as classified by the Economic Research Service of the United States Department of Agriculture.\n**(4) Interstate or foreign air transportation**\nThe term interstate or foreign air transportation has the meaning given the term interstate air transportation in section 40102, including transportation in foreign air commerce.\n##### (b) Clerical amendment\nThe analysis for chapter 449 of title 49, United States Code, is amended by adding at the end the following:\n44949. Restriction on air transportation of adult roosters .\n#### 5. Enforcement\nThe Secretary of Transportation shall enforce this Act and the amendments made by this Act, in coordination with the Federal Aviation Administration, and may promulgate such regulations as are necessary to carry out its provisions. Violations shall be subject to civil penalties under chapter 463 of title 49, United States Code.\n#### 6. Rule of construction\nNothing in this Act or the amendments made by this Act shall be construed to preempt any State law that provides greater protections for aviation safety or imposes stricter restrictions on the air transportation of live animals.\n#### 7. Effective date\nThis Act and the amendments made by this Act shall take effect 180 days after the date of enactment.",
      "versionDate": "2026-02-04",
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
        "updateDate": "2026-03-09T18:31:40Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7371ih.xml"
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
      "title": "No Flight, No Fight Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T11:08:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Flight, No Fight Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T11:08:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To restrict the air transportation of certain live animals in interstate and foreign commerce to enhance aviation safety, biosecurity, and operational efficiency in civil aviation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-06T11:03:30Z"
    }
  ]
}
```
