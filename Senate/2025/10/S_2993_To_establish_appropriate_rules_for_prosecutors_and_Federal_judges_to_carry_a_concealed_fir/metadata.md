# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2993?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2993
- Title: Protect Our Prosecutors and Judges Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2993
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2026-02-11T12:03:25Z
- Update date including text: 2026-02-11T12:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2993",
    "number": "2993",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Protect Our Prosecutors and Judges Act of 2025",
    "type": "S",
    "updateDate": "2026-02-11T12:03:25Z",
    "updateDateIncludingText": "2026-02-11T12:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
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
      "actionDate": "2025-10-09",
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
            "date": "2025-10-09T15:00:12Z",
            "name": "Referred To"
          },
          {
            "date": "2025-10-09T15:00:12Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-10-27",
      "state": "NC"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "TN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "OK"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "WV"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-01-28",
      "state": "TX"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MO"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2993is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2993\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish appropriate rules for prosecutors and Federal judges to carry a concealed firearm.\n#### 1. Short title\nThis Act may be cited as the Protect Our Prosecutors and Judges Act of 2025 .\n#### 2. Authority to carry a concealed firearm for prosecutors and Federal judges\n##### (a) Current prosecutors and Federal judges\nSection 926B of title 18, United States Code, is amended\u2014\n**(1)**\nin the section heading, by inserting , qualified prosecutors, and qualified Federal judges after qualified law enforcement officers ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby inserting , a qualified prosecutor, or a qualified Federal judge after qualified law enforcement officer ; and\n**(B)**\nby striking subsection (d) and inserting subsection (c) ;\n**(3)**\nby striking subsections (c), (d), and (e) and inserting the following:\n(c) The identification required by this subsection is\u2014 (1) with respect to a qualified law enforcement officer, the photographic identification issued by the governmental agency for which the individual is employed that identifies the employee as a police officer or law enforcement officer of the agency; (2) with respect to a qualified prosecutor\u2014 (A) the photographic identification issued by the governmental agency by which the individual is employed that identifies the employee as a prosecutor of the agency; and (B) a certification\u2014 (i) if agency employing the qualified prosecutor has authorized the qualified prosecutor to carry a firearm, that indicates that the qualified prosecutor has been tested or otherwise found by the agency to meet the active duty standards for qualification in firearms training as established by the agency to carry a firearm of the same type as the concealed firearm; or (ii) if the agency employing the qualified prosecutor has not authorized the qualified prosecutor to carry a firearm, issued by the State in which the qualified prosecutor resides or by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State that indicates that the qualified prosecutor has been tested or otherwise found by the State or certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State to have met\u2014 (I) the active duty standards for qualification in firearms training, as established by the State, to carry a firearm of the same type as the concealed firearm; or (II) if the State has not established such standards, standards set by any law enforcement agency within that State to carry a firearm of the same type as the concealed firearm; and (3) with respect to a qualified Federal judge\u2014 (A) photographic identification issued by the Federal Government that identifies the individual as a Federal judge; and (B) a certification issued by the State in which the Federal judge resides or by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State that indicates that the individual has been tested or otherwise found by the State or certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State to have met\u2014 (i) the active duty standards for qualification in firearms training, as established by the State, to carry a firearm of the same type as the concealed firearm; or (ii) if the State has not established such standards, standards set by any law enforcement agency within that State to carry a firearm of the same type as the concealed firearm. ;\n**(4)**\nby redesignating subsection (f) as subsection (d); and\n**(5)**\nby adding at the end the following:\n(e) As used in this section\u2014 (1) the term firearm \u2014 (A) except as provided in this paragraph, has the same meaning as in section 921 of this title; (B) includes ammunition not expressly prohibited by Federal law or subject to the provisions of the National Firearms Act; and (C) does not include\u2014 (i) any machinegun (as defined in section 5845 of the National Firearms Act); (ii) any firearm silencer (as defined in section 921 of this title); and (iii) any destructive device (as defined in section 921 of this title); (2) the term qualified Federal judge means an individual who\u2014 (A) is serving in a position as a judge that is established under article I, III, or IV of the Constitution of the United States; (B) is not the subject of a pending impeachment inquiry or trial; (C) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (D) is not prohibited by Federal law from receiving a firearm; (3) the term qualified law enforcement officer means an employee of a governmental agency who\u2014 (A) is authorized by law to engage in or supervise the prevention, detection, investigation or prosecution of, or the incarceration of any person for, any violation of law, and has statutory powers of arrest or apprehension under section 807(b) of title 10, United States Code (article 7(b) of the Uniform Code of Military Justice); (B) is authorized by the agency to carry a firearm; (C) is not the subject of any disciplinary action by the agency which could result in suspension or loss of police powers; (D) meets standards, if any, established by the agency which require the employee to regularly qualify in the use of a firearm; (E) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (F) is not prohibited by Federal law from receiving a firearm; and (4) the term qualified prosecutor means an individual who\u2014 (A) is a full-time employee of an agency of the Federal Government or a State or unit of local government who\u2014 (i) is continually licensed to practice law; and (ii) prosecutes criminal or juvenile delinquency cases at the Federal, State, or local level (including supervision, education, or training of other persons prosecuting such cases); (B) is not the subject of any disciplinary action by the agency which could result in suspension; (C) meets standards, if any, established by the agency which require the employee to regularly qualify in the use of a firearm; (D) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (E) is not prohibited by Federal law from receiving a firearm. .\n##### (b) Retired prosecutors and Federal judges\nSection 926C of title 18, United States Code, is amended\u2014\n**(1)**\nin the section heading, by inserting , qualified retired prosecutors, and qualified retired Federal judges after qualified retired law enforcement officers ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby inserting , a qualified retired prosecutor, or a qualified Federal judge after qualified law enforcement officer ; and\n**(B)**\nby striking subsection (d) and inserting subsection (c) ; and\n**(3)**\nby striking subsections (c), (d), and (e) and inserting the following:\n(c) The identification required by this subsection is\u2014 (1) with respect to a qualified retired law enforcement officer\u2014 (A) a photographic identification issued by the agency from which the individual separated from service as a law enforcement officer that identifies the person as having been employed as a police officer or law enforcement officer and indicates that the individual has, not less recently than 1 year before the date the individual is carrying the concealed firearm, been tested or otherwise found by the agency to meet the active duty standards for qualification in firearms training as established by the agency to carry a firearm of the same type as the concealed firearm; or (B) (i) a photographic identification issued by the agency from which the individual separated from service as a law enforcement officer that identifies the person as having been employed as a police officer or law enforcement officer; and (ii) a certification issued by the State in which the individual resides or by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State that indicates that the individual has, not less than 1 year before the date the individual is carrying the concealed firearm, been tested or otherwise found by the State or certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State to have met\u2014 (I) the active duty standards for qualification in firearms training, as established by the State, to carry a firearm of the same type as the concealed firearm; or (II) if the State has not established such standards, standards set by any law enforcement agency within that State to carry a firearm of the same type as the concealed firearm; (2) with respect to a qualified retired prosecutor\u2014 (A) the photographic identification issued by the governmental agency by which the individual was employed that identifies the individual as a former prosecutor of the agency; and (B) a certification issued by the State in which the qualified retired prosecutor resides or by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State that indicates that the qualified retired prosecutor has, not less than 1 year before the date the qualified retired prosecutor is carrying the concealed firearm, been tested or otherwise found by the State or certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State to have met\u2014 (i) the active duty standards for qualification in firearms training, as established by the State, to carry a firearm of the same type as the concealed firearm; or (ii) if the State has not established such standards, standards set by any law enforcement agency within that State to carry a firearm of the same type as the concealed firearm; and (3) with respect to a qualified retired Federal judge\u2014 (A) photographic identification issued by the Federal Government that identifies the individual as a former Federal judge; and (B) a certification issued by the State in which the Federal judge resides or by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State that indicates that the individual has, not less than 1 year before the date the individual is carrying the concealed firearm, been tested or otherwise found by the State or certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State to have met\u2014 (i) the active duty standards for qualification in firearms training, as established by the State, to carry a firearm of the same type as the concealed firearm; or (ii) if the State has not established such standards, standards set by any law enforcement agency within that State to carry a firearm of the same type as the concealed firearm. (d) As used in this section\u2014 (1) the term firearm \u2014 (A) except as provided in this paragraph, has the same meaning as in section 921 of this title; (B) includes ammunition not expressly prohibited by Federal law or subject to the provisions of the National Firearms Act; and (C) does not include\u2014 (i) any machinegun (as defined in section 5845 of the National Firearms Act); (ii) any firearm silencer (as defined in section 921 of this title); and (iii) any destructive device (as defined in section 921 of this title); (2) the term qualified retired Federal judge means an individual who\u2014 (A) separated from service in good standing from service in a position as a judge that was established under article I, III, or IV of the Constitution of the United States; (B) (i) has not been officially found by a qualified medical professional employed by the Federal Government to be unqualified for reasons relating to mental health and as a result of this finding will not be issued the photographic identification as described in subsection (c)(3); and (ii) has not entered into an agreement with the Federal Government in which that individual acknowledges he or she is not qualified under this section for reasons relating to mental health and for those reasons will not receive or accept the photographic identification as described in subsection (c)(3); (C) during the most recent 12-month period, has met, at the expense of the individual, the standards for qualification in firearms training for active law enforcement officers, as determined by the State in which the individual resides or, if the State has not established such standards, either a law enforcement agency within the State in which the individual resides or the standards used by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State; (D) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (E) is not prohibited by Federal law from receiving a firearm; (3) the term qualified retired law enforcement officer means an individual who\u2014 (A) separated from service in good standing from service with a public agency as a law enforcement officer; (B) before such separation, was authorized by law to engage in or supervise the prevention, detection, investigation, or prosecution of, or the incarceration of any person for, any violation of law, and had statutory powers of arrest or apprehension under section 807(b) of title 10, United States Code (article 7(b) of the Uniform Code of Military Justice); (C) (i) before such separation, served as a law enforcement officer for an aggregate of 10 years or more; or (ii) separated from service with such agency, after completing any applicable probationary period of such service, due to a service-connected disability, as determined by such agency; (D) during the most recent 12-month period, has met, at the expense of the individual, the standards for qualification in firearms training for active law enforcement officers, as determined by the former agency of the individual, the State in which the individual resides or, if the State has not established such standards, either a law enforcement agency within the State in which the individual resides or the standards used by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State; (E) (i) has not been officially found by a qualified medical professional employed by the agency to be unqualified for reasons relating to mental health and as a result of this finding will not be issued the photographic identification as described in subsection (c)(1); or (ii) has not entered into an agreement with the agency from which the individual is separating from service in which that individual acknowledges he or she is not qualified under this section for reasons relating to mental health and for those reasons will not receive or accept the photographic identification as described in subsection (c)(1); (F) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (G) is not prohibited by Federal law from receiving a firearm; and (4) the term qualified retired prosecutor means an individual who\u2014 (A) separated from service in good standing from service as a full-time employee of an agency of the Federal Government or a State or unit of local government who\u2014 (i) during such service was continually licensed to practice law; and (ii) prosecuted criminal or juvenile delinquency cases at the Federal, State, or local level (including supervision, education, or training of other persons prosecuting such cases); (B) before such separation, served as described in subparagraph (A) for an aggregate of 10 years or more; (C) (i) has not been officially found by a qualified medical professional employed by the agency to be unqualified for reasons relating to mental health and as a result of this finding will not be issued the photographic identification as described in subsection (c)(2); and (ii) has not entered into an agreement with the agency in which that individual acknowledges he or she is not qualified under this section for reasons relating to mental health and for those reasons will not receive or accept the photographic identification as described in subsection (c)(2); (D) during the most recent 12-month period, has met, at the expense of the individual, the standards for qualification in firearms training for active law enforcement officers, as determined by the former agency of the individual, the State in which the individual resides or, if the State has not established such standards, either a law enforcement agency within the State in which the individual resides or the standards used by a certified firearms instructor that is qualified to conduct a firearms qualification test for active duty officers within that State; (E) is not under the influence of alcohol or another intoxicating or hallucinatory drug or substance; and (F) is not prohibited by Federal law from receiving a firearm. .\n##### (c) Technical and conforming amendment\nThe table of sections for chapter 44 of title 18, United States Code, is amended by striking the items relating to sections 926B and 926C and inserting the following:\n926B. Carrying of concealed firearms by qualified law enforcement officers, qualified prosecutors, and qualified Federal judges. 926C. Carrying of concealed firearms by qualified retired law enforcement officers, qualified retired prosecutors, and qualified retired Federal judges. .\n##### (d) Regulations\nThe Attorney General and the Director of the Administrative Office of United States Courts may promulgate such regulations as are necessary to carry out the amendments made by this section.",
      "versionDate": "2025-10-09",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-12-08T18:07:53Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2993is.xml"
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
      "title": "Protect Our Prosecutors and Judges Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protect Our Prosecutors and Judges Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-21T11:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish appropriate rules for prosecutors and Federal judges to carry a concealed firearm.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-21T11:18:16Z"
    }
  ]
}
```
