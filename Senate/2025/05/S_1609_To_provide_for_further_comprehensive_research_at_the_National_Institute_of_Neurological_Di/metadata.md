# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1609
- Title: Ellie’s Law
- Congress: 119
- Bill type: S
- Bill number: 1609
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2026-03-18T11:03:18Z
- Update date including text: 2026-03-18T11:03:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1609",
    "number": "1609",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Ellie\u2019s Law",
    "type": "S",
    "updateDate": "2026-03-18T11:03:18Z",
    "updateDateIncludingText": "2026-03-18T11:03:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-06",
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
            "date": "2025-05-06T16:22:34Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-06T16:22:34Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "OK"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "RI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "MA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "MN"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1609is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1609\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Blumenthal (for himself and Mr. Mullin ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for further comprehensive research at the National Institute of Neurological Disorders and Stroke on unruptured intracranial aneurysms.\n#### 1. Short title\nThis Act may be cited as the Ellie Helton, Lisa Colagrossi, Kristen Shafer Englert, Teresa Anne Lawrence, and Jennifer Sedney Focused Research Act or Ellie\u2019s Law .\n#### 2. Findings\nThe Congress makes the following findings:\n**(1)**\nAn estimated 6,800,000 people in the United States, or 1 in 50 people, have an unruptured brain aneurysm.\n**(2)**\nEach year, an estimated 30,000 people in the United States suffer a brain aneurysm rupture. Ruptured brain aneurysms are fatal in about 50 percent of cases. Of those who survive, about 66 percent suffer some permanent neurological deficit.\n**(3)**\nBrain aneurysms are more likely to occur in women, and are nearly twice as likely to rupture in African American and Hispanic individuals. Ellie\u2019s Law represents all those who have been affected and died due to a ruptured brain aneurysm, and their loved ones. The personal stories of individuals who have recently experienced a brain aneurysm rupture include the following:\n**(A)**\nEllie Helton. On July 16, 2014, Ellie Helton, a vibrant, loving 14-year-old from Apex, North Carolina, passed away as a result of a ruptured aneurysm, stunning her parents, 2 sisters, and many, many loved ones. A day earlier, on her second day of high school, she woke up with a terrible headache after a plum-sized aneurysm on her brain stem ruptured. While she suffered headaches throughout her life, she was never diagnosed. Ellie was an avid reader and excellent student, loved the arts, and was incredibly creative. She had an unwavering, constant love for the family and friends in her life.\n**(B)**\nLisa Colagrossi. On March 20, 2015, Lisa Colagrossi\u2014WABC Eyewitness News reporter, wife of 17 years, and mother of 2 sons\u2014unexpectedly passed away at the age of 49 years after suffering a massive ruptured brain aneurysm. Despite experiencing one of the classic warning signs of a brain aneurysm (the worst headache of my life ), Lisa\u2019s passing came as a tremendous shock to her family and friends, who did not know what a brain aneurysm was, let alone its signs and symptoms. She is remembered for being a loving wife, a mother, and a successful reporter, and for her love of the New York Rangers.\n**(C)**\nKristen Shafer Englert. On November 24, 2013, Kristen Shafer Englert, a devoted wife, mother, daughter, sister, aunt, and friend passed away from a ruptured brain aneurysm at the age of 25, just weeks after giving birth to her son. Prior to her passing, she went to the emergency room with symptoms of a brain aneurysm and was sent home without a scan. Kristen was a dedicated teacher who loved children. She was thrilled to become a mother. Sadly, she got to experience motherhood only for a few short days. Kristen\u2019s family members have been dedicated advocates for brain aneurysm awareness and research since her passing.\n**(D)**\nTeresa Anne Lawrence. On December 8, 1983, Teresa Anne Lawrence, a devoted mother of 3, beloved wife, and staple of her community, collapsed while visiting her son's school. She had been struggling with and taking medication for hypertension for several years. At age 34, after being unconscious for 4 days, she passed away as a result of a brain aneurysm. Her loving husband and extended family were left to raise their children, whom Teresa cherished so much.\n**(E)**\nJennifer Sedney. On December 25, 2013, Jennifer Sedney, a beautiful, accomplished young woman, passed away suddenly at the age of 27 from a ruptured brain aneurysm. Her only symptom was the worst headache of her life , which none of her friends or family realized was a symptom of a potentially fatal condition. Jenny was a jogger, a disciplined exerciser, and a successful health care consultant and had recently launched a health blog founded on 3 principles\u2014 bee curious, bee radiant, bee well . Her brother, mother, father, and a large devoted network of friends and relatives remember her every day.\n**(4)**\nBrain aneurysm ruptures have a significant fiscal impact on survivors, caretakers, and the health care community. The annual estimated pre-insurance direct cost of brain aneurysm ruptures to patients is approximately $2,000,000,000, and the median expected patient payment is $144,000. The length of stay in an intensive care unit is the largest driver of cost for brain aneurysm ruptures, and estimates do not reflect indirect costs, including travel, food, childcare, and wage losses for the patient and caretakers.\n**(5)**\nDespite the widespread prevalence of this condition and the high societal cost it imposes on the Nation, the Federal Government only spends approximately $2.94 per year on brain aneurysm research for each person afflicted with a brain aneurysm.\n**(6)**\nThe first 3 iterations of the International Study on Unruptured Intracranial Aneurysms (ISUIA) have advanced researchers\u2019 and clinicians\u2019 understanding of how to most effectively manage and treat unruptured intracranial aneurysms.\n#### 3. Funding\n##### (a) Authorization of appropriations\nTo conduct or support further comprehensive research on unruptured intracranial aneurysms, studying a broader patient population diversified by age, sex, and race, there is authorized to be appropriated to the National Institute of Neurological Disorders and Stroke $10,000,000 for each of fiscal years 2026 through 2030, to remain available through September 30, 2033.\n##### (b) Supplement, not supplant\nAny funds made available pursuant to this section shall supplement, not supplant, other funding made available for research on brain aneurysms.",
      "versionDate": "2025-05-06",
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
        "actionDate": "2025-04-07",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2678",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ellie\u2019s Law",
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
        "name": "Health",
        "updateDate": "2025-05-22T17:14:32Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1609is.xml"
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
      "title": "Ellie\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ellie\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ellie Helton, Lisa Colagrossi, Kristen Shafer Englert, Teresa Anne Lawrence, and Jennifer Sedney Focused Research Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-16T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for further comprehensive research at the National Institute of Neurological Disorders and Stroke on unruptured intracranial aneurysms.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-16T03:18:25Z"
    }
  ]
}
```
