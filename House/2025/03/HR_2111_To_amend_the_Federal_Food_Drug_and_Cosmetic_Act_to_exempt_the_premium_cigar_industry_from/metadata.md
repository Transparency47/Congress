# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2111?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2111
- Title: To amend the Federal Food, Drug, and Cosmetic Act to exempt the premium cigar industry from certain regulations.
- Congress: 119
- Bill type: HR
- Bill number: 2111
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-02-10T09:05:22Z
- Update date including text: 2026-02-10T09:05:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2111",
    "number": "2111",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000032",
        "district": "19",
        "firstName": "Byron",
        "fullName": "Rep. Donalds, Byron [R-FL-19]",
        "lastName": "Donalds",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend the Federal Food, Drug, and Cosmetic Act to exempt the premium cigar industry from certain regulations.",
    "type": "HR",
    "updateDate": "2026-02-10T09:05:22Z",
    "updateDateIncludingText": "2026-02-10T09:05:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:00:25Z",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "NV"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "CA"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "NV"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "sponsorshipWithdrawnDate": "2025-04-29",
      "state": "LA"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NY"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "PA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-06-30",
      "state": "AL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NY"
    },
    {
      "bioguideId": "J000304",
      "district": "13",
      "firstName": "Ronny",
      "fullName": "Rep. Jackson, Ronny [R-TX-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "IL"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2111ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2111\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Donalds (for himself, Mr. Langworthy , Ms. Titus , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to exempt the premium cigar industry from certain regulations.\n#### 1. Findings\nThe Congress finds the following:\n**(1)**\nPremium cigars comprise only 1 percent of all cigars sold in the United States.\n**(2)**\nMost manufacturers of premium cigars are family-owned small businesses.\n**(3)**\nPremium cigars are typically sold in age-controlled retail establishments, such as tobacco specialty shops or cigar bars.\n**(4)**\nAt the request of the Food and Drug Administration and the National Institutes of Health, the National Academies of Sciences, Engineering, and Medicine (in this section referred to as the NASEM ) convened an expert committee to examine 4 premium cigar topics: product characteristics, patterns of use, marketing and perceptions, and health effects.\n**(5)**\nThe NASEM expert committee produced a resulting report, published in 2022 and titled Premium Cigars: Patterns of Use, Marketing, and Health Effects , which among other things, identified numerous facts regarding premium cigar use.\n**(6)**\nThe NASEM expert committee found that premium cigars are only used by about 1 percent of the United States adult population.\n**(7)**\nThe NASEM expert committee found that premium cigar use is less common among youth than among other users and only 0.6 percent of those who reported smoking a premium cigar were under 18 years of age.\n**(8)**\nThe NASEM expert committee found that premium cigar use is less common among women, non-Hispanic Black persons, and persons with less than a high school education than other users.\n**(9)**\nThe NASEM expert committee found that premium cigar users are less likely to smoke cigarettes or other cigar types concurrently than other cigar type users.\n**(10)**\nThe NASEM expert committee found that the frequency and intensity of smoking is lower for premium cigars compared to other types of cigars and cigarettes.\n**(11)**\nThe NASEM expert committee found that as compared to users of other types of cigars, premium cigar users are more likely to be never or former cigarette smokers.\n**(12)**\nThe NASEM expert committee found that there is strongly suggestive evidence that the health consequences of premium cigar smoking overall are likely to be less than those of smoking other types of cigars because the majority of premium cigar smokers are nondaily or occasional users and because they are unlikely to inhale the smoke.\n**(13)**\nThe NASEM expert committee found that premium cigars are used virtually exclusively by adults, premium cigar use is extremely limited, and premium cigar use poses less physical risk than the use of other tobacco products.\n**(14)**\nThe definition of premium cigar used by the NASEM expert committee is broader and would encompass a larger class of cigars than the definition adopted by Judge Amit P. Mehta, of the United States District Court for the District of Columbia, in a recent decision striking the latest attempt by the Food and Drug Administration to regulate premium cigars.\n**(15)**\nThe narrower definition adopted by Judge Mehta is the definition that would apply if this bill were enacted.\n**(16)**\nThe District Court concluded that the few health risks posed by premium cigars can be regulated at the State level.\n#### 2. Exemption of premium cigars from certain tobacco regulation in Federal Food, Drug, and Cosmetic Act\nSection 201(rr) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(rr) ) is amended by adding at the end the following:\n(6) (A) The term tobacco product does not mean a premium cigar. (B) In clause (A), the term premium cigar means a cigar that\u2014 (i) is wrapped in whole tobacco leaf; (ii) contains a 100 percent leaf tobacco binder; (iii) contains at least 50 percent (of the filler by weight) long filler tobacco (whole tobacco leaves that run the length of the cigar); (iv) is handmade or hand rolled, meaning no machinery was used apart from simple tools, such as scissors to cut the tobacco prior to rolling; (v) has no filter, nontobacco tip, or nontobacco mouthpiece; (vi) does not have a characterizing flavor other than tobacco; (vii) contains only tobacco, water, and vegetable gum with no other ingredients or additives; and (viii) weighs more than 6 pounds per 1,000 units. .",
      "versionDate": "2025-03-14",
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
        "name": "Health",
        "updateDate": "2025-03-31T15:40:41Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2111ih.xml"
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
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to exempt the premium cigar industry from certain regulations.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:46Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act to exempt the premium cigar industry from certain regulations.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:08Z"
    }
  ]
}
```
