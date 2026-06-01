# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3904?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3904
- Title: U.S. Bicycle Production and Assembly Act
- Congress: 119
- Bill type: HR
- Bill number: 3904
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2026-05-12T08:06:16Z
- Update date including text: 2026-05-12T08:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3904",
    "number": "3904",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "U.S. Bicycle Production and Assembly Act",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:16Z",
    "updateDateIncludingText": "2026-05-12T08:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NJ"
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
      "sponsorshipDate": "2025-09-08",
      "state": "CA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "VA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3904ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3904\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Buchanan (for himself and Mr. Thompson of California ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Harmonized Tariff Schedule of the United States to modify temporarily certain rates of duty for bicycle assembly and manufacturing parts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the U.S. Bicycle Production and Assembly Act .\n#### 2. Temporary duty suspension for bicycle assembly and manufacturing parts\n##### (a) In general\nSubchapter III of chapter 99 of the Harmonized Tariff Schedule of the United States (hereinafter referred to as the HTS ) is amended by inserting the following new heading in numerical sequence:\n9903.87.11 Parts of bicycles imported for use in the assembly or manufacturing of complete bicycles, under the terms of U.S. Note 34 to this subchapter Free No change No change .\n##### (b) Definition and applicability\nThe U.S. Notes to subchapter III of chapter 99 of the HTS are amended by adding at the end the following:\n34. (a) For purposes of heading 9903.87.11, the term parts of bicycles means parts, accessories, or specific components that are\u2014 (i) classified in the tariff provisions described in subdivision (f) of this note; and (ii) imported into the customs territory of the United States for assembly or manufacturing into complete tricycles or bicycles, including bicycles without a motor (provided for in heading 8712.00) and bicycles with an electric motor (provided for in subheading 8711.60.00), and bicycle trailers (provided for in subheading 8716.40.00). (b) For purposes of heading 9903.87.11, the term assembly or manufacturing of complete bicycles means the fitting or joining together of fabricated components classifiable as parts of bicycles (as such term is defined under subdivision (a) of this note) using standard industry processes to produce bicycles suitable for sale or consumption with only minor assembly or adjustment required by the end user. (c) Any importer claiming entry of parts of bicycles under heading 9903.87.11 must\u2014 (i) certify at the time of entry to the satisfaction of U.S. Customs and Border Protection (hereinafter referred to as CBP ) that such parts will be used in the assembly or manufacturing of complete bicycles (as such term is defined under subdivision (b) of this note); and (ii) provide appropriate documentation to CBP upon the completion of final assembly or manufacturing of such bicycles or at such other time as CBP may establish. (d) Parts of bicycles for which entry is claimed under heading 9903.87.11 shall be excluded from any additional duties under section 301 of the Trade Act of 1974 ( 19 U.S.C. 2411 ) or any other provision of law based on the classification of such parts under any of chapters 1 through 97. (e) Notwithstanding subdivision (d) of this note, parts of bicycles may be included in a claim for duty-free entry under heading 9903.87.11 if such parts are properly classified in any 8-digit tariff heading or subheading described in subdivision (f) of this note when such parts are entered on or after the date on which an additional duty under section 301 of the Trade Act of 1974 ( 19 U.S.C. 2411 ) or any other provision of law is no longer effective. (f) The 8-digit tariff headings and subheadings described in this subdivision are the following: 3923.50.00 3926.90.96 4011.50.00 4013.20.00 4908.10.00 7315.11.00 7326.90.25 8501.31.40 8501.31.50 8501.31.60 8507.20.80 8507.30.80 8507.50.00 8507.60.00 8512.90.40 8543.70.45 8714.91.20 8714.91.30 8714.91.50 8714.91.90 8714.92.10 8714.92.50 8714.93.28 8714.93.35 8714.93.70 8714.94.30 8714.94.90 8714.95.00 8714.96.10 8714.96.50 8714.96.90 8714.99.10 8714.99.50 8714.99.60 8714.99.80 .\n##### (c) Report\nNot later than 5 years after the date of the enactment of this Act, the Chair of the United States International Trade Commission shall submit to the Chairman and Ranking Member of the Committee on Ways and Means of the House of Representatives and the Chairman and Ranking Member of the Committee on Finance of the Senate a report describing the effects of the amendments made under subsections (a) and (b) and evaluating the contribution and effectiveness of such amendments toward increasing the assembly and manufacturing of bicycles within the United States to meet the following goals:\n**(1)**\n2,000,000 bicycles annually in the United States within 5 years of such date of enactment.\n**(2)**\n5,000,000 bicycles annually in the United States within 10 years of such date of enactment.\n##### (d) Rulemaking\nThe Commissioner of U.S. Customs and Border Protection may prescribe rules for the appropriate administration of this Act, and the amendments made by this Act, and requiring such information as such Commissioner considers necessary from any importer who claims duty-free entry under heading 9903.87.11 of the HTS, as amended by subsection (a).\n##### (e) Effective date\nThis Act, and the amendments made by this Act, shall take effect during the 10-year period beginning on the date of the enactment of this Act.",
      "versionDate": "2025-06-11",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-07-23T13:35:26Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3904ih.xml"
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
      "title": "U.S. Bicycle Production and Assembly Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S. Bicycle Production and Assembly Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T09:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Harmonized Tariff Schedule of the United States to modify temporarily certain rates of duty for bicycle assembly and manufacturing parts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T09:18:23Z"
    }
  ]
}
```
