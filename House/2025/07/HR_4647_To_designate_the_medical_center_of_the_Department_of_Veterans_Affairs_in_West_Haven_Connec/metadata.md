# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4647?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4647
- Title: Captain Paul W. Bud Bucha VA Medical Center Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4647
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-20T09:06:43Z
- Update date including text: 2025-12-20T09:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-19 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4647",
    "number": "4647",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Captain Paul W. Bud Bucha VA Medical Center Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-20T09:06:43Z",
    "updateDateIncludingText": "2025-12-20T09:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-19",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-19T19:05:50Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4647ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4647\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. DeLauro introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo designate the medical center of the Department of Veterans Affairs in West Haven, Connecticut, as the Captain Paul W. Bud Bucha VA Medical Center .\n#### 1. Short title\nThis Act may be cited as the Captain Paul W. Bud Bucha VA Medical Center Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nPaul W. Bud Bucha was born on August 1, 1943, in Washington, DC.\n**(2)**\nPaul W. Bud Bucha, a recipient of the Medal of Honor and an advocate for veterans, is an American hero.\n**(3)**\nPaul W. Bud Bucha, the son of a colonel in the Army, spent his childhood in California, Germany, Indiana, Japan, and St. Louis, Missouri.\n**(4)**\nPaul W. Bud Bucha turned down several scholarships for both academics and athletics and instead enrolled in the United States Military Academy at West Point, New York. He went on to be a two-time All-American and captain of the West Point swim team. In 1965, he graduated in the top 5 percent of his class and number two in Military Order of Merit.\n**(5)**\nPaul W. Bud Bucha earned a Masters of Business Administration from Stanford University in 1967, all while completing Airborne and Ranger training between academic years.\n**(6)**\nPaul W. Bud Bucha reported for duty with the 101st Airborne Division at Fort Campbell, Kentucky, to prepare for deployment to Vietnam as part of Operation Eagle Thrust in November 1967.\n**(7)**\nPaul W. Bud Bucha was appointed commander of Company D, 3rd Battalion, 187th Infantry Regiment. His company was the last rifle company to be formed during an Army expansion. He jokingly recalled that his recruits were men who had flunked basic infantry tasks, former prisoners, and guys with master\u2019s degrees in Elizabethan literature . He took pride in his company, dubbed the clerks and jerks . They went on to become one of the most decorated units by the end of the war.\n**(8)**\nPaul W. Bud Bucha distinguished himself with extraordinary heroism while leading 89 men on a reconnaissance mission near Phuoc Vinh, Vietnam, from March 16th through 18th, 1968. As part of the Tet Offensive, his unit was dropped by helicopter and his men set out to repel attacks by North Vietnamese and Viet Cong forces. As the sun set on March 18, 1968, he and his men advanced into a dense jungle and found themselves outgunned by approximately 1,500 enemy troops. Under attack, he crawled 40 yards through the hail of fire and singlehandedly destroyed a machine-gun bunker with grenades, all while sustaining a shrapnel wound. He then orchestrated an overnight offensive, directing his men to spread out, throw grenades, and unleash heavy fire. He made the enemy believe they were a much larger force. His leadership led to the defeat of a superior Vietnamese stronghold, leaving 156 enemy dead. Come morning, he guided the medical evacuation of three air-ambulance loads of seriously wounded personnel.\n**(9)**\nPresident Richard Nixon presented the Medal of Honor to Paul W. Bud Bucha in a ceremony at the White House in 1970.\n**(10)**\nPaul W. Bud Bucha originally wanted to turn down the Medal of Honor because he did not feel deserving. In Vietnam, he asked his men to trust him and, in turn, promised to bring them home safe. 10 of his men were killed on the night of March 18, 1968. Paul W. Bud Bucha ultimately accepted the Medal of Honor in their memory, saying it belongs to his men.\n**(11)**\nPaul W. Bud Bucha resigned his Army commission in 1972.\n**(12)**\nPaul W. Bud Bucha was an active member of several veterans service organizations (commonly referred to as VSOs ), including the American Legion, Veterans of Foreign Wars, Disabled American Veterans, and the Vietnam Veterans of America. He generously served on the board of directors of Homes for Our Troops, a VSO that builds specially adapted custom homes for severely injured veterans. He also served as Chairman of the Advisory Committee on Veterans Employment and Training Services at the Department of Labor.\n**(13)**\nPaul W. Bud Bucha used his voice for veterans struggling with mental health. He believed that all veterans, whether they have 4 stars or no stripes, man or woman , would be touched by post-traumatic stress. He used the term post-traumatic stress to acknowledge the impact of combat experiences on the mental health of veterans and he intentionally left out the word disorder to help destigmatize their struggle.\n**(14)**\nPaul W. Bud Bucha battled post-traumatic stress on his own for 42 years before courageously seeking help at the medical center of the Department of Veterans Affairs in West Haven, Connecticut. In the final years of his life, Paul W. Bud Bucha also received neurological care at that medical center. His family expressed deep gratitude for the compassionate and skilled care he received, especially recognizing the leadership of Dr. Huned Patwa, Chief of Staff, and Dr. Becky Rhoads, Executive Director. His family also commended the dedicated neurologists, psychiatrists, and oncologists who supported him as his health declined.\n**(15)**\nPaul W. Bud Bucha spent the last two weeks of his life at the medical center of the Department in West Haven, Connecticut, and passed away from complications of Alzheimer\u2019s disease on July 31, 2024. In his final act of courage and service, he donated his brain to the Center for Human Brain Discovery at Yale University.\n#### 3. Designation of Captain Paul W. Bud Bucha VA Medical Center\n##### (a) In general\nThe medical center of the Department of Veterans Affairs in West Haven, Connecticut, or any successor location for such medical center, shall after the date of the enactment of this Act be known and designated as the Captain Paul W. Bud Bucha Department of Veterans Affairs Medical Center or the Captain Paul W. Bud Bucha VA Medical Center .\n##### (b) Reference\nAny reference in any law, regulation, map, document, paper, or other record of the United States to the medical center referred to in subsection (a) shall be considered to be a reference to the Captain Paul W. Bud Bucha VA Medical Center.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-08-08",
        "actionTime": "11:45:07",
        "text": "Held at the desk."
      },
      "number": "2682",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Captain Paul W. 'Bud' Bucha VA Medical Center Act of 2025",
      "type": "S"
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
            "name": "Congressional tributes",
            "updateDate": "2025-08-08T15:14:33Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-08-08T15:14:33Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-08-08T15:14:33Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-08-08T15:14:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-08-01T15:18:43Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4647ih.xml"
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
      "title": "Captain Paul W. Bud Bucha VA Medical Center Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-01T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Captain Paul W. Bud Bucha VA Medical Center Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-01T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the medical center of the Department of Veterans Affairs in West Haven, Connecticut, as the \"Captain Paul W. 'Bud' Bucha VA Medical Center\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-01T05:18:33Z"
    }
  ]
}
```
