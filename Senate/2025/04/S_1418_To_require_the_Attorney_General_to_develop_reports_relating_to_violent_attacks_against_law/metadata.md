# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1418
- Title: Improving Law Enforcement Officer Safety and Wellness Through Data Act
- Congress: 119
- Bill type: S
- Bill number: 1418
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-04-28T11:03:21Z
- Update date including text: 2026-04-28T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1418",
    "number": "1418",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Improving Law Enforcement Officer Safety and Wellness Through Data Act",
    "type": "S",
    "updateDate": "2026-04-28T11:03:21Z",
    "updateDateIncludingText": "2026-04-28T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
            "date": "2025-04-10T16:09:38Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-10T16:09:38Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NC"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NH"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "LA"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1418is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1418\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Grassley (for himself, Mr. Luj\u00e1n , Mr. Tillis , Ms. Hassan , and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo require the Attorney General to develop reports relating to violent attacks against law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Law Enforcement Officer Safety and Wellness Through Data Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThere has been a rise in anti-police rhetoric and a corresponding rise in violence against law enforcement officers.\n**(2)**\nIn 2022, a total of 60 police officers were feloniously killed in the line of duty.\n**(3)**\nNearly 30 percent of police officer killings in 2022 were caused by unprovoked attacks or ambushes on officers.\n**(4)**\nLaw enforcement officers bravely put themselves at risk for the betterment of society.\n**(5)**\nA data collection that represents the full circumstances surrounding violent attacks and ambush attacks on law enforcement officers is vital for the provision of needed Federal resources to Federal, State, and local law enforcement officers.\n**(6)**\nPolice suffer assaults and other offenses that do not rise to the level of Law Enforcement Officers Killed and Assaulted or National Incident-Based Reporting System reporting due to the frequency of such incidents, lower risk to officers, and minimal administrative resources to report such frequent events.\n**(7)**\nThe mental health of law enforcement officers has suffered due to overwork, recruitment issues, and the general stress of their work.\n**(8)**\nThe people of the United States will always remember the victims of these hateful attacks against law enforcement officers and stand in solidarity with individuals affected by these senseless tragedies and incidents of hate that have affected law enforcement communities and their families.\n**(9)**\nThe United States must demonstrate to its brave law enforcement officers that they are important, valued, and respected.\n**(10)**\nCongress has made a commitment to helping communities protect the lives of their police officers, as evidenced by the Bulletproof Vest Partnership Grant Program Reauthorization Act of 2015 ( Public Law 114\u2013155 ; 130 Stat. 389) and other laws.\n**(11)**\nSubsection (c) of the Uniform Federal Crime Reporting Act of 1988 ( 34 U.S.C. 41303(c) ) requires the Attorney General to acquire, collect, classify, and preserve national data on Federal criminal offenses as part of the Uniform Crime Reports and requires all Federal departments and agencies that investigate criminal activity to report details about crime within their respective jurisdiction to the Attorney General in a uniform matter and on a form prescribed by the Attorney General .\n#### 3. Attacks on law enforcement officers reporting requirement\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Attorney General, in consultation with the Director of the Federal Bureau of Investigation, the Director of the National Institute of Justice, and the Director of the Criminal Justice Information Services Division of the Federal Bureau of Investigation, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that includes\u2014\n**(1)**\nthe number of offenders that intentionally target law enforcement officers because of their status as law enforcement officers;\n**(2)**\nthe number of incidents reported to the Law Enforcement Officers Killed and Assaulted Data Collection that occur through the coordinated actions of 2 or more parties;\n**(3)**\na description of the Federal response to ambushes and violent attacks on Federal law enforcement officers;\n**(4)**\na detailed survey of what State and local responses are to ambushes and violent attacks on State and local law enforcement officers;\n**(5)**\nrecommendations for improving State, local, and Federal responses to ambushes and violent attacks on law enforcement officers;\n**(6)**\na detailed survey of Federal and State-based training programs that law enforcement officers receive in preparation for violent attacks, including ambush attacks;\n**(7)**\nan analysis of the effectiveness of the programs described in paragraph (6) in preparing law enforcement officers for violent attacks, including ambush attacks;\n**(8)**\nrecommendations on how to improve State, local, and Federal training programs for law enforcement officers relating to ambush attacks;\n**(9)**\nan analysis of, with respect to the Patrick Leahy Bulletproof Vest Partnership under part Y of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10530 et seq. )\u2014\n**(A)**\nthe efficacy of the Partnership in distributing protective gear to law enforcement officers across the United States, including any location-specific limitations to the distribution under such Partnership; and\n**(B)**\nthe general limitations of the Partnership, including any location-specific limitations to the distributions under the Partnership, considering the fact that law enforcement officers are suffering from ambush attacks;\n**(10)**\nan analysis of the ability of the Department of Justice to combine the Law Enforcement Officers Killed and Assaulted Data Collection and a 09C Justifiable Homicide report for officer-involved shooting reports and any roadblocks to producing a clear report with such information;\n**(11)**\nan analysis of the ability of the Criminal Justice Information Services of the Federal Bureau of Investigation to expand data collection to include a suspect offender\u2019s level of injury at the time of a reported Law Enforcement Officers Killed and Assaulted Data Collection incident;\n**(12)**\nan analysis of the existence and extent of, and reasons for, disparities in the availability and reporting of data between\u2014\n**(A)**\ndata relating to ambush attacks against law enforcement officers; and\n**(B)**\nother types of violent crime data; and\n**(13)**\nan analysis of any additional legislative tools or authorities that may be helpful or necessary to assist in deterring ambush attacks against law enforcement officers.\n##### (b) Development\nIn developing the report required under subsection (a), the Attorney General, the Director of the Federal Bureau of Investigation, the Director of the National Institute of Justice, and the Director of the Criminal Justice Information Services Division of the Federal Bureau of Investigation, shall consult relevant stakeholders, including\u2014\n**(1)**\nFederal, State, Tribal, and local law enforcement agencies; and\n**(2)**\nnongovernmental organizations, international organizations, academies, or other entities.\n#### 4. Aggression against law enforcement officers reporting requirement\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Attorney General, in consultation with the Director of the Federal Bureau of Investigation and the Director of the National Institute of Justice, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on\u2014\n**(1)**\nan analysis of the ability to implement a new category in the Uniform Crime Reporting System and the National Incident-Based Reporting System on aggressive actions, conduct, or other trauma-inducing incidents against law enforcement officers that, as of the date of enactment of this Act, are not reported in such systems;\n**(2)**\nthe level of detail the category described in paragraph (1) would include and the standard of evidence that would be used for any reported incidents;\n**(3)**\nan analysis of how to engage State and local law enforcement agencies in reporting the data described in paragraph (1), despite the fact that such data is beyond the standard crime-based reporting to the systems described in paragraph (1);\n**(4)**\nan analysis of potential uses by the Department of Justice and any component agencies of the Department of Justice of the data described in paragraph (1);\n**(5)**\nan analysis of the existence and extent of, and reasons for, disparities in the availability and reporting of data between\u2014\n**(A)**\ndata relating to aggressive actions or other trauma-inducing incidents against law enforcement officers that do not rise to the level of crimes; and\n**(B)**\nother types of violent crime data; and\n**(6)**\nan analysis of additional legislative tools or authorities that may be helpful or necessary to assist in deterring aggressive actions, conduct, or other trauma-inducing incidents against law enforcement officers.\n##### (b) Development\nIn developing the report under subsection (a), the Attorney General, the Director of the Federal Bureau of Investigation, and the Director of the National Institute of Justice shall consult relevant stakeholders, including\u2014\n**(1)**\nFederal, State, Tribal, and local law enforcement agencies; and\n**(2)**\nnongovernmental organizations, international organizations, academies, or other entities.\n#### 5. Mental health and wellness reporting requirement\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Attorney General, in consultation with the Director of the Federal Bureau of Investigation and the Director of the National Institute of Justice, shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report on\u2014\n**(1)**\nthe types, frequency, and severity of mental health and stress-related responses of law enforcement officers to aggressive actions or other trauma-inducing incidents against law enforcement officers;\n**(2)**\nmental health and stress-related resources or programs that are available to law enforcement officers at the Federal, State, and local levels, especially peer-to-peer programs;\n**(3)**\nthe extent to which law enforcement officers use the resources or programs described in paragraph (2);\n**(4)**\nthe availability of, or need for, mental health screening within Federal, State, and local law enforcement agencies; and\n**(5)**\nadditional legislative tools or authorities that may be helpful or necessary to assist in assessing, monitoring, and improving the mental health and wellness of Federal, State, and local law enforcement officers.\n##### (b) Development\nIn developing the report required under subsection (a), the Attorney General, the Director of the Federal Bureau of Investigation, and the Director of the National Institute of Justice shall consult relevant stakeholders, including\u2014\n**(1)**\nFederal, State, Tribal and local law enforcement agencies; and\n**(2)**\nnongovernmental organizations, international organizations, academies, or other entities.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-05-19",
        "text": "Received in the Senate and Read twice and referred to the Committee on the Judiciary."
      },
      "number": "2240",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving Law Enforcement Officer Safety and Wellness Through Data Act",
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
        "updateDate": "2025-05-20T12:16:16Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1418is.xml"
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
      "title": "Improving Law Enforcement Officer Safety and Wellness Through Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Law Enforcement Officer Safety and Wellness Through Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Attorney General to develop reports relating to violent attacks against law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:27Z"
    }
  ]
}
```
