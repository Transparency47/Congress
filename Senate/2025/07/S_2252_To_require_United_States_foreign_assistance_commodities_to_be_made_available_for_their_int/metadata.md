# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2252?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2252
- Title: Saving Lives and Taxpayer Dollars Act
- Congress: 119
- Bill type: S
- Bill number: 2252
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-02-04T12:03:15Z
- Update date including text: 2026-02-04T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2252",
    "number": "2252",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Saving Lives and Taxpayer Dollars Act",
    "type": "S",
    "updateDate": "2026-02-04T12:03:15Z",
    "updateDateIncludingText": "2026-02-04T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
        "item": [
          {
            "date": "2025-07-10T16:56:35Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-10T16:56:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "HI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "DE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "VA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "ME"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "AK"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NJ"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "CO"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2252is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2252\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mrs. Shaheen (for herself and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require United States foreign assistance commodities to be made available for their intended purposes before they expire.\n#### 1. Short title\nThis Act may be cited as the Saving Lives and Taxpayer Dollars Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nForeign assistance commodities, including food, medicine, family planning products, and vaccines, provide critical support to people who are recovering from the aftermath of natural disasters, fleeing conflict or war, residing in refugee camps, or living in developing communities with limited access to health care.\n**(2)**\nUnited States investments in global health bolster economic growth for partner countries, produce returns on investment for the United States economy, create an estimated 600,000 jobs in the United States, and generated an estimated $104,000,000,000 in economic activity during the 15-year period between 2007 and 2022.\n**(3)**\nReliable access to vaccines and medications, including pre-exposure prophylaxis and antiretroviral drugs to prevent the spread of HIV and vaccines to prevent the transmission of communicable diseases such as polio and drug-resistant tuberculosis, make everyone safer.\n**(4)**\nUnited States food assistance benefits United States farmers, ranchers, and agribusinesses, while addressing global food insecurity. United States farmers annually supply an estimated 40 percent of all international food assistance, which is valued at approximately $2,000,000,000.\n**(5)**\nGreater access to family planning products and services has the potential to prevent up to 30 percent of the 295,000 annual maternal deaths and save the lives of approximately 1,400,000 children who are younger than 5 years old.\n**(6)**\nThe voluntary destruction of foreign assistance commodities intended for beneficiaries at risk of food insecurity and famine, sexual violence, maternal and infant death and disease is unethical and contrary to United States interests and moral obligations.\n#### 3. Prohibition on the destruction of foreign assistance products and commodities\nSection 102 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151\u20131 ) is amended\u2014\n**(1)**\nin subsection (b), by adding at the end the following:\n(18) Perishable and nonperishable foreign assistance commodities and products, including medicine, vaccines, medical devices, food and food commodities that are procured, managed, controlled, or held in warehouses, ships, shipping containers, or any other storage facility, by the United States Government or by a foreign assistance implementing partner of the United States Government shall be made available to intended beneficiaries, including through donation, for their intended purpose and before the date on which such commodities and products spoil or expire. ; and\n**(2)**\nby adding at the end the following:\n(d) (1) In this subsection\u2014 (A) the term appropriate congressional committees means\u2014 (i) the Committee on Foreign Relations of the Senate ; (ii) the Committee on Appropriations of the Senate ; (iii) the Committee on Foreign Affairs of the House of Representatives ; and (iv) the Committee on Appropriations of the House of Representatives ; and (B) the term commodity means a product or commodity referred to in subsection (b)(18). (2) If any commodity is in the possession or control of a foreign assistance implementing partner of the United States, the Secretary of State, the Secretary of Agriculture, or the Administrator of the United States Agency for International Development, as appropriate, shall release such funds as may be necessary, on an expedited basis, to ensure the delivery or donation of the commodity to intended beneficiaries before the applicable spoilage or expiration date. (3) No commodity may be destroyed unless every effort has been made to sell, donate, or otherwise make available the commodity, whichever is more likely to ensure the commodity will be received and utilized by its intended beneficiaries, before the applicable spoilage or expiration date. (4) (A) Not later than 90 days after the date of the enactment of the Saving Lives and Taxpayer Dollars Act , and annually thereafter, the Secretary of State, in coordination with the Administrator of the United States Agency for International Development and the Secretary of Agriculture, as appropriate, shall submit a report to the appropriate congressional committees that describes any commodity that expired, spoiled, or was destroyed without delivery to an intended beneficiary. (B) The report required under subparagraph (A) shall include, for each expired, spoiled, or destroyed commodity \u2014 (i) a description of all negotiations, planning, and efforts to make the commodity available to intended beneficiaries; (ii) the reason the commodity was not made available to intended beneficiaries; (iii) the purpose of the commodity and the geographic locations of all intended beneficiaries of such commodity; (iv) the procured and market value of the commodity; and (v) the cost incurred to destroy the commodity. .",
      "versionDate": "2025-07-10",
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
        "actionDate": "2025-07-17",
        "text": "Referred to the House Committee on Foreign Affairs."
      },
      "number": "4516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Saving Lives and Taxpayer Dollars Act",
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
        "name": "International Affairs",
        "updateDate": "2025-08-01T17:22:31Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2252is.xml"
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
      "title": "Saving Lives and Taxpayer Dollars Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-04T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Saving Lives and Taxpayer Dollars Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require United States foreign assistance commodities to be made available for their intended purposes before they expire.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:24Z"
    }
  ]
}
```
